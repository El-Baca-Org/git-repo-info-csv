# -*- coding: utf-8 -*-

import requests
import csv
import argparse
import sys
import tkinter as tk
from tkinter import messagebox

def fetch_repos(username):
    url = f"https://api.github.com/users/{username}/repos"
    response = requests.get(url)

    if response.status_code == 404:
        raise ValueError(f"User '{username}' not found.")
    elif response.status_code == 403:
        raise PermissionError("API rate limit exceeded. Please try again later.")
    elif response.status_code != 200:
        raise Exception(f"Failed to fetch repositories. HTTP Status: {response.status_code}")

    return response.json()

def save_to_csv(repos, output_filename='github_repos.csv'):
    with open(output_filename, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        # CSV headers (Turkish)
        writer.writerow(['Repo Adı', 'Açıklama', 'Dil', 'Yıldız Sayısı', 'Fork Sayısı', 'URL'])

        for repo in repos:
            writer.writerow([
                repo.get('name'),
                repo.get('description'),
                repo.get('language'),
                repo.get('stargazers_count'),
                repo.get('forks_count'),
                repo.get('html_url')
            ])

def run_gui():
    root = tk.Tk()
    root.title("GitHub Repo Fetcher")
    root.geometry("400x200")

    # GUI Elements
    tk.Label(root, text="GitHub Username:").pack(pady=10)
    username_entry = tk.Entry(root, width=30)
    username_entry.pack()

    tk.Label(root, text="Output Filename:").pack(pady=10)
    output_entry = tk.Entry(root, width=30)
    output_entry.insert(0, "github_repos.csv")
    output_entry.pack()

    def on_fetch():
        username = username_entry.get().strip()
        output = output_entry.get().strip()

        if not username:
            messagebox.showerror("Error", "Please enter a GitHub username.")
            return

        if not output:
            output = "github_repos.csv"

        try:
            repos = fetch_repos(username)
            save_to_csv(repos, output)
            messagebox.showinfo("Success", f"Repository information for '{username}' has been successfully written to {output}")
        except ValueError as ve:
            messagebox.showerror("Error", str(ve))
        except PermissionError as pe:
            messagebox.showerror("Error", str(pe))
        except Exception as e:
            messagebox.showerror("Error", f"Unexpected Error: {e}")

    fetch_button = tk.Button(root, text="Fetch and Save", command=on_fetch)
    fetch_button.pack(pady=20)

    root.mainloop()

def main_cli():
    parser = argparse.ArgumentParser(description="Download GitHub Repo Information in CSV Format")
    parser.add_argument("--username", type=str, help="GitHub username to fetch repositories for")
    parser.add_argument("--output", type=str, default="github_repos.csv", help="Output CSV filename")

    # If no arguments are provided, launch GUI
    if len(sys.argv) == 1:
        run_gui()
        return

    args = parser.parse_args()

    if not args.username:
        parser.error("The --username argument is required when running in CLI mode.")

    try:
        repos = fetch_repos(args.username)
        save_to_csv(repos, args.output)
        print(f"Repository information for '{args.username}' has been successfully written to {args.output}")
    except ValueError as ve:
        print(f"Error: {ve}", file=sys.stderr)
    except PermissionError as pe:
        print(f"Error: {pe}", file=sys.stderr)
    except Exception as e:
        print(f"Unexpected Error: {e}", file=sys.stderr)

if __name__ == "__main__":
    main_cli()
