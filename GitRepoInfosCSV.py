# -*- coding: utf-8 -*-

import requests
import csv

def fetch_and_save_repos(username, output_file='github_repos.csv'):
    # GitHub API URL'si
    url = f"https://api.github.com/users/{username}/repos"

    try:
        # API'den verileri çek
        response = requests.get(url)
        response.raise_for_status()
        repos = response.json()

        # CSV dosyasına yazma
        with open(output_file, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)

            # CSV başlıkları
            writer.writerow(['Repo Adı', 'Açıklama', 'Dil', 'Yıldız Sayısı', 'Fork Sayısı', 'URL'])

            # Her repo için bilgileri yaz
            for repo in repos:
                writer.writerow([
                    repo.get('name'),
                    repo.get('description'),
                    repo.get('language'),
                    repo.get('stargazers_count'),
                    repo.get('forks_count'),
                    repo.get('html_url')
                ])

        print(f"Repo bilgileri {output_file} dosyasına yazıldı.")
        return True
    except Exception as e:
        print(f"An error occurred: {e}")
        return False

def run_gui():
    import tkinter as tk
    from tkinter import messagebox

    def on_fetch():
        username = entry_username.get().strip()
        output_file = entry_output.get().strip()

        if not username:
            messagebox.showerror("Error", "Please enter a GitHub username.")
            return

        if not output_file:
            output_file = 'github_repos.csv'

        success = fetch_and_save_repos(username, output_file)
        if success:
            messagebox.showinfo("Success", f"Repository information saved to {output_file}.")
        else:
            messagebox.showerror("Error", "Failed to fetch repository information. Check console for details.")

    root = tk.Tk()
    root.title("GitHub Repo Fetcher")

    tk.Label(root, text="GitHub Username:").grid(row=0, column=0, padx=10, pady=10, sticky='w')
    entry_username = tk.Entry(root, width=30)
    entry_username.grid(row=0, column=1, padx=10, pady=10)

    tk.Label(root, text="Output CSV Filename:").grid(row=1, column=0, padx=10, pady=10, sticky='w')
    entry_output = tk.Entry(root, width=30)
    entry_output.insert(0, "github_repos.csv")
    entry_output.grid(row=1, column=1, padx=10, pady=10)

    btn_fetch = tk.Button(root, text="Fetch and Save", command=on_fetch)
    btn_fetch.grid(row=2, column=0, columnspan=2, pady=20)

    root.mainloop()

if __name__ == "__main__":
    import argparse
    import sys

    parser = argparse.ArgumentParser(description="Fetch GitHub repository information for a user and save it to a CSV file.")
    parser.add_argument("--username", help="GitHub username to fetch repositories for.", required=False)
    parser.add_argument("--output", help="Output CSV filename.", default="github_repos.csv", required=False)

    # If arguments are provided (other than the script name itself), use CLI mode.
    # Otherwise, launch the GUI.
    if len(sys.argv) > 1:
        args = parser.parse_args()
        if args.username:
            fetch_and_save_repos(args.username, args.output)
        else:
            parser.print_help()
    else:
        run_gui()
