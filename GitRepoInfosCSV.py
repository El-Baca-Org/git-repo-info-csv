# -*- coding: utf-8 -*-

import requests
import csv
import argparse
import sys
import tkinter as tk
from tkinter import messagebox, filedialog

def fetch_and_save_repos(username, output_filename):
    # GitHub API URL
    url = f"https://api.github.com/users/{username}/repos"

    try:
        # Fetch data from API
        response = requests.get(url)

        # Check if the request was successful
        if response.status_code == 404:
            return False, f"User '{username}' not found."
        elif response.status_code == 403:
            return False, "GitHub API rate limit exceeded. Please try again later."

        response.raise_for_status()

        repos = response.json()

        # Write to CSV file
        with open(output_filename, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)

            # CSV headers (kept in Turkish for backward compatibility)
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

        return True, f"Repository info successfully written to {output_filename}"

    except requests.exceptions.RequestException as e:
        return False, f"Network error occurred: {e}"
    except IOError as e:
        return False, f"File write error occurred: {e}"
    except Exception as e:
        return False, f"An unexpected error occurred: {e}"

def run_gui():
    def submit():
        username = entry_username.get().strip()
        if not username:
            messagebox.showwarning("Input Error", "Please enter a GitHub username.")
            return

        # Choose where to save the file
        output_filename = filedialog.asksaveasfilename(
            defaultextension=".csv",
            initialfile=f"{username}_repos.csv",
            title="Save CSV File",
            filetypes=(("CSV files", "*.csv"), ("All files", "*.*"))
        )

        if not output_filename:
            return # User cancelled

        success, message = fetch_and_save_repos(username, output_filename)
        if success:
            messagebox.showinfo("Success", message)
        else:
            messagebox.showerror("Error", message)

    root = tk.Tk()
    root.title("GitHub Repo Info Downloader")
    root.geometry("400x150")

    frame = tk.Frame(root, padx=20, pady=20)
    frame.pack(expand=True, fill="both")

    label_username = tk.Label(frame, text="GitHub Username:")
    label_username.pack(anchor="w", pady=(0, 5))

    entry_username = tk.Entry(frame, width=40)
    entry_username.pack(fill="x", pady=(0, 15))

    btn_submit = tk.Button(frame, text="Fetch & Save Repos", command=submit)
    btn_submit.pack()

    root.mainloop()

def main():
    parser = argparse.ArgumentParser(description="Fetch GitHub repository information for a specific user and save it to a CSV file.")
    parser.add_argument("--username", help="The GitHub username to fetch repositories for.", type=str)
    parser.add_argument("--output", help="The output CSV filename (default: github_repos.csv).", type=str, default="github_repos.csv")

    # If no arguments are passed, show GUI
    if len(sys.argv) == 1:
        run_gui()
    else:
        args = parser.parse_args()
        if not args.username:
            print("Error: --username is required when using the command line.")
            parser.print_help()
            sys.exit(1)

        print(f"Fetching repositories for '{args.username}'...")
        success, message = fetch_and_save_repos(args.username, args.output)

        if success:
            print(f"Success: {message}")
        else:
            print(f"Error: {message}")
            sys.exit(1)

if __name__ == "__main__":
    main()
