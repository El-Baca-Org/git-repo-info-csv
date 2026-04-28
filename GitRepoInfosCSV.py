# -*- coding: utf-8 -*-

import requests
import csv
import argparse
import sys
import tkinter as tk
from tkinter import messagebox

def fetch_and_save_repos(username, output_file='github_repos.csv'):
    # GitHub API URL
    url = f"https://api.github.com/users/{username}/repos"

    # Fetch data from API
    response = requests.get(url)

    if response.status_code != 200:
        error_msg = f"Failed to fetch repositories for {username}. Status code: {response.status_code}"
        if response.status_code == 403:
            error_msg += " (Rate limit might be exceeded)"
        elif response.status_code == 404:
            error_msg += " (User not found)"
        print(error_msg)
        return False, error_msg

    repos = response.json()

    # Write to CSV
    try:
        with open(output_file, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)

            # CSV headers (in Turkish for backward compatibility)
            writer.writerow(['Repo Adı', 'Açıklama', 'Dil', 'Yıldız Sayısı', 'Fork Sayısı', 'URL'])

            # Write repo info
            for repo in repos:
                writer.writerow([
                    repo.get('name', ''),
                    repo.get('description', ''),
                    repo.get('language', ''),
                    repo.get('stargazers_count', 0),
                    repo.get('forks_count', 0),
                    repo.get('html_url', '')
                ])
        print(f"Repository info successfully written to {output_file}.")
        return True, f"Repository info successfully written to {output_file}."
    except Exception as e:
        error_msg = f"An error occurred while writing to CSV: {e}"
        print(error_msg)
        return False, error_msg

def launch_gui():
    def on_submit():
        username = username_entry.get().strip()
        output_file = output_entry.get().strip()

        if not username:
            messagebox.showwarning("Input Error", "Please enter a GitHub username.")
            return

        if not output_file:
            output_file = "github_repos.csv"

        if not output_file.endswith('.csv'):
            output_file += '.csv'

        success, message = fetch_and_save_repos(username, output_file)
        if success:
            messagebox.showinfo("Success", message)
        else:
            messagebox.showerror("Error", message)

    root = tk.Tk()
    root.title("GitHub Repo Info Downloader")
    root.geometry("400x200")
    root.resizable(False, False)

    # Username Label and Entry
    tk.Label(root, text="GitHub Username:").pack(pady=(15, 5))
    username_entry = tk.Entry(root, width=40)
    username_entry.pack()

    # Output File Label and Entry
    tk.Label(root, text="Output File (default: github_repos.csv):").pack(pady=(15, 5))
    output_entry = tk.Entry(root, width=40)
    output_entry.pack()
    output_entry.insert(0, "github_repos.csv")

    # Submit Button
    tk.Button(root, text="Download Info", command=on_submit, width=20, bg="#4CAF50", fg="black").pack(pady=20)

    # Center the window
    root.eval('tk::PlaceWindow . center')
    root.mainloop()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Download GitHub repository information to a CSV file.")
    parser.add_argument("--username", help="GitHub username to fetch repositories for.", type=str)
    parser.add_argument("--output", help="Output CSV filename (default: github_repos.csv).", type=str, default="github_repos.csv")

    args = parser.parse_args()

    # If username is provided via CLI, use CLI mode
    if args.username:
        output = args.output
        if not output.endswith('.csv'):
            output += '.csv'
        fetch_and_save_repos(args.username, output)
    else:
        # Otherwise, launch the GUI
        launch_gui()
