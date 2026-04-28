# -*- coding: utf-8 -*-

import requests
import csv
import sys
import argparse
import tkinter as tk
from tkinter import messagebox

def get_repos(username):
    url = f"https://api.github.com/users/{username}/repos"
    response = requests.get(url)

    if response.status_code == 200:
        return response.json()
    elif response.status_code == 404:
        print(f"Error: User '{username}' not found.")
        return None
    elif response.status_code == 403:
        print("Error: GitHub API rate limit exceeded.")
        return None
    else:
        print(f"Error: Failed to fetch data. HTTP Status Code: {response.status_code}")
        return None

def write_to_csv(repos, output_file='github_repos.csv'):
    if not repos:
        return False

    try:
        with open(output_file, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
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
        print(f"Repo bilgileri {output_file} dosyasına yazıldı.")
        return True
    except Exception as e:
        print(f"Error writing to CSV: {e}")
        return False

def run_gui():
    def submit():
        username = username_entry.get()
        output_file = output_entry.get() or "github_repos.csv"

        if not username:
            messagebox.showwarning("Input Error", "Please enter a GitHub username.")
            return

        repos = get_repos(username)
        if repos:
            if write_to_csv(repos, output_file):
                messagebox.showinfo("Success", f"Repository information saved to {output_file}.")
            else:
                messagebox.showerror("Error", "Failed to write to CSV file.")
        else:
            messagebox.showerror("Error", "Failed to fetch data. Ensure the username is correct or check your API limit.")

    root = tk.Tk()
    root.title("GitHub Repo Info Downloader")
    root.geometry("400x200")

    tk.Label(root, text="GitHub Username:").pack(pady=(20, 5))
    username_entry = tk.Entry(root, width=40)
    username_entry.pack()

    tk.Label(root, text="Output Filename (Optional):").pack(pady=(10, 5))
    output_entry = tk.Entry(root, width=40)
    output_entry.insert(0, "github_repos.csv")
    output_entry.pack()

    tk.Button(root, text="Download", command=submit).pack(pady=20)

    root.mainloop()

def main():
    parser = argparse.ArgumentParser(description="Download GitHub Repo Information in CSV Format")
    parser.add_argument("--username", help="GitHub username")
    parser.add_argument("--output", default="github_repos.csv", help="Output CSV filename")

    # Check if there are arguments passed, if not open GUI
    if len(sys.argv) > 1:
        args = parser.parse_args()
        if args.username:
            repos = get_repos(args.username)
            if repos:
                write_to_csv(repos, args.output)
        else:
            parser.print_help()
    else:
        run_gui()

if __name__ == "__main__":
    main()
