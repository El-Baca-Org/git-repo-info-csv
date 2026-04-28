# -*- coding: utf-8 -*-

import requests
import csv
import argparse
import tkinter as tk
from tkinter import messagebox

def fetch_and_save_repos(username, output_filename='github_repos.csv'):
    # GitHub API URL'si
    url = f"https://api.github.com/users/{username}/repos"

    # API'den verileri çek
    response = requests.get(url)

    if response.status_code == 403:
        print("Rate limit exceeded. Please try again later.")
        return False
    elif response.status_code != 200:
        print(f"Error fetching data: HTTP {response.status_code}")
        return False

    repos = response.json()

    # CSV dosyasına yazma
    with open(output_filename, mode='w', newline='', encoding='utf-8') as file:
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

    print(f"Repo bilgileri {output_filename} dosyasına yazıldı.")
    return True

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Fetch GitHub repositories for a user and save to CSV.")
    parser.add_argument("--username", help="GitHub username to fetch repositories for")
    parser.add_argument("--output", help="Output CSV filename", default="github_repos.csv")

    args = parser.parse_args()

    if args.username:
        fetch_and_save_repos(args.username, args.output)
    else:
        def on_fetch():
            username = username_entry.get().strip()
            output = output_entry.get().strip() or "github_repos.csv"

            if not username:
                messagebox.showerror("Error", "Please enter a GitHub username.")
                return

            success = fetch_and_save_repos(username, output)
            if success:
                messagebox.showinfo("Success", f"Repository information has been written to {output}.")
            else:
                messagebox.showerror("Error", "Failed to fetch data. Check rate limits or the username.")

        root = tk.Tk()
        root.title("GitHub Repo Fetcher")

        tk.Label(root, text="GitHub Username:").grid(row=0, column=0, padx=10, pady=10, sticky="e")
        username_entry = tk.Entry(root, width=30)
        username_entry.grid(row=0, column=1, padx=10, pady=10)

        tk.Label(root, text="Output File Name:").grid(row=1, column=0, padx=10, pady=10, sticky="e")
        output_entry = tk.Entry(root, width=30)
        output_entry.insert(0, "github_repos.csv")
        output_entry.grid(row=1, column=1, padx=10, pady=10)

        fetch_button = tk.Button(root, text="Fetch and Save", command=on_fetch)
        fetch_button.grid(row=2, column=0, columnspan=2, pady=20)

        root.mainloop()
