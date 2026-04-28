# -*- coding: utf-8 -*-

import requests
import csv
import argparse
import sys
import tkinter as tk
from tkinter import messagebox, filedialog

def fetch_and_save_repos(username, output_file):
    # GitHub API URL
    url = f"https://api.github.com/users/{username}/repos"

    try:
        # Fetch data from API
        response = requests.get(url)
        response.raise_for_status()  # Check for errors like 403 or 404
        repos = response.json()

        # Check if the user has no repos or we got an unexpected response
        if not isinstance(repos, list):
            return False, f"Unexpected response from GitHub API. Please check the username."

        # Write to CSV file
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

        return True, f"Repository info successfully written to {output_file}."
    except requests.exceptions.HTTPError as e:
        return False, f"HTTP Error: {e}"
    except requests.exceptions.RequestException as e:
        return False, f"Request Error: {e}"
    except Exception as e:
        return False, f"An unexpected error occurred: {e}"


def run_gui():
    def download_data():
        username = username_entry.get().strip()
        if not username:
            messagebox.showwarning("Input Error", "Please enter a GitHub username.")
            return

        output_file = filedialog.asksaveasfilename(
            defaultextension=".csv",
            initialfile="github_repos.csv",
            title="Save CSV as",
            filetypes=(("CSV files", "*.csv"), ("All files", "*.*"))
        )

        if not output_file:
            return  # User cancelled the save dialog

        success, message = fetch_and_save_repos(username, output_file)
        if success:
            messagebox.showinfo("Success", message)
        else:
            messagebox.showerror("Error", message)

    root = tk.Tk()
    root.title("GitHub Repo Fetcher")
    root.geometry("400x150")

    tk.Label(root, text="GitHub Username:").pack(pady=10)

    username_entry = tk.Entry(root, width=30)
    username_entry.pack(pady=5)

    download_button = tk.Button(root, text="Fetch and Save Repos", command=download_data)
    download_button.pack(pady=10)

    root.mainloop()


def run_cli():
    parser = argparse.ArgumentParser(description="Fetch GitHub repositories for a user and save to CSV.")
    parser.add_argument("--username", required=True, help="GitHub username to fetch repositories for")
    parser.add_argument("--output", default="github_repos.csv", help="Output CSV filename (default: github_repos.csv)")

    args = parser.parse_args()

    success, message = fetch_and_save_repos(args.username, args.output)
    if success:
        print(message)
    else:
        print(f"Error: {message}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    if len(sys.argv) > 1:
        run_cli()
    else:
        run_gui()
