# -*- coding: utf-8 -*-

import requests
import csv

import argparse
import sys

def fetch_and_save_repos(username, output_file='github_repos.csv'):
    """Fetches GitHub repository information for a given user and saves it to a CSV."""
    url = f"https://api.github.com/users/{username}/repos"

    try:
        response = requests.get(url)
        response.raise_for_status() # Raise an exception for bad status codes
        repos = response.json()

        if not isinstance(repos, list):
             print(f"Error: API returned an unexpected format. Message: {repos.get('message', 'Unknown error')}")
             return False

        with open(output_file, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            # Headers in Turkish
            writer.writerow(['Repo Adı', 'Açıklama', 'Dil', 'Yıldız Sayısı', 'Fork Sayısı', 'URL'])

            for repo in repos:
                writer.writerow([
                    repo.get('name', ''),
                    repo.get('description', ''),
                    repo.get('language', ''),
                    repo.get('stargazers_count', 0),
                    repo.get('forks_count', 0),
                    repo.get('html_url', '')
                ])

        print(f"Repository information successfully written to {output_file}.")
        return True

    except requests.exceptions.RequestException as e:
        print(f"Error fetching data from GitHub API: {e}")
        return False
    except IOError as e:
        print(f"Error writing to file {output_file}: {e}")
        return False


def run_gui():
    """Runs the Tkinter GUI."""
    import tkinter as tk
    from tkinter import messagebox

    def on_fetch():
        username = entry_username.get().strip()
        if not username:
            messagebox.showwarning("Input Error", "Please enter a GitHub username.")
            return

        output_file = entry_output.get().strip() or 'github_repos.csv'

        # Simple feedback
        btn_fetch.config(state=tk.DISABLED, text="Fetching...")
        root.update()

        success = fetch_and_save_repos(username, output_file)

        btn_fetch.config(state=tk.NORMAL, text="Fetch and Save")

        if success:
            messagebox.showinfo("Success", f"Repository information successfully written to {output_file}.")
        else:
            messagebox.showerror("Error", "Failed to fetch or save data. Check the console for details or verify the username/rate limits.")

    root = tk.Tk()
    root.title("GitHub Repo Fetcher")
    root.geometry("400x200")
    root.resizable(False, False)

    tk.Label(root, text="GitHub Username:").pack(pady=(20, 5))
    entry_username = tk.Entry(root, width=40)
    entry_username.pack()

    tk.Label(root, text="Output File (optional, default: github_repos.csv):").pack(pady=(10, 5))
    entry_output = tk.Entry(root, width=40)
    entry_output.pack()

    btn_fetch = tk.Button(root, text="Fetch and Save", command=on_fetch)
    btn_fetch.pack(pady=20)

    root.mainloop()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Fetch GitHub repositories for a user and save to CSV.")
    parser.add_argument('--username', type=str, help='The GitHub username to fetch repositories for.')
    parser.add_argument('--output', type=str, default='github_repos.csv', help='The output CSV filename (default: github_repos.csv).')

    # Check if arguments were provided (sys.argv > 1 because [0] is the script name)
    if len(sys.argv) > 1:
        args = parser.parse_args()
        if args.username:
            fetch_and_save_repos(args.username, args.output)
        else:
            print("Error: --username is required when using CLI.")
            parser.print_help()
    else:
        # Launch GUI if no arguments are provided
        run_gui()