# -*- coding: utf-8 -*-

import requests
import csv
import argparse
import tkinter as tk
from tkinter import filedialog, messagebox, ttk

def fetch_repos(username):
    url = f"https://api.github.com/users/{username}/repos"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    elif response.status_code == 404:
        raise Exception(f"User '{username}' not found.")
    elif response.status_code == 403:
        raise Exception("API rate limit exceeded. Please try again later.")
    else:
        raise Exception(f"Failed to fetch repositories. Status code: {response.status_code}")

def save_to_csv(repos, output_file='github_repos.csv'):
    with open(output_file, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
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
    return output_file

def run_gui():
    def submit():
        username = entry_username.get().strip()
        if not username:
            messagebox.showwarning("Input Error", "Please enter a GitHub username.")
            return

        try:
            repos = fetch_repos(username)

            output_file = filedialog.asksaveasfilename(
                defaultextension=".csv",
                filetypes=[("CSV files", "*.csv"), ("All files", "*.*")],
                initialfile="github_repos.csv",
                title="Save CSV File As"
            )

            if output_file:
                save_to_csv(repos, output_file)
                messagebox.showinfo("Success", f"Repo info successfully written to {output_file}.")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    root = tk.Tk()
    root.title("GitHub Repo Info Downloader")
    root.geometry("400x150")

    frame = ttk.Frame(root, padding="10")
    frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

    label_username = ttk.Label(frame, text="GitHub Username:")
    label_username.grid(row=0, column=0, pady=10, sticky=tk.W)

    entry_username = ttk.Entry(frame, width=30)
    entry_username.grid(row=0, column=1, pady=10, sticky=tk.W)

    btn_download = ttk.Button(frame, text="Download", command=submit)
    btn_download.grid(row=1, column=0, columnspan=2, pady=10)

    root.mainloop()

def main():
    parser = argparse.ArgumentParser(description="Download GitHub Repo Information in CSV Format")
    parser.add_argument("--username", help="GitHub username")
    parser.add_argument("--output", default="github_repos.csv", help="Output CSV filename")

    args = parser.parse_args()

    if args.username:
        try:
            repos = fetch_repos(args.username)
            output_file = save_to_csv(repos, args.output)
            print(f"Repo bilgileri {output_file} dosyasına yazıldı.")
        except Exception as e:
            print(f"Error: {e}")
    else:
        run_gui()

if __name__ == "__main__":
    main()