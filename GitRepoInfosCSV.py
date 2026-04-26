# -*- coding: utf-8 -*-

import requests
import csv

def fetch_and_save_repos(username, output_file='github_repos.csv'):
    # GitHub API URL'si
    url = f"https://api.github.com/users/{username}/repos"

    # API'den verileri çek
    response = requests.get(url)

    if response.status_code != 200:
        print(f"Failed to fetch repositories for user: {username}. Status code: {response.status_code}")
        return False

    repos = response.json()

    # CSV dosyasına yazma
    with open(output_file, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)

        # CSV başlıkları
        writer.writerow(['Repo Adı', 'Açıklama', 'Dil', 'Yıldız Sayısı', 'Fork Sayısı', 'URL'])

        # Her repo için bilgileri yaz
        for repo in repos:
            writer.writerow([repo['name'], repo['description'], repo['language'], repo['stargazers_count'], repo['forks_count'], repo['html_url']])

    print(f"Repo bilgileri {output_file} dosyasına yazıldı.")
    return True

import argparse

def run_gui():
    import tkinter as tk
    from tkinter import messagebox
    def submit():
        username = entry_username.get()
        if not username:
            messagebox.showwarning("Input Error", "Please enter a GitHub username.")
            return

        success = fetch_and_save_repos(username)
        if success:
            messagebox.showinfo("Success", f"Repository info for '{username}' saved to github_repos.csv")
        else:
            messagebox.showerror("Error", f"Failed to fetch repositories for user: {username}.")

    root = tk.Tk()
    root.title("GitHub Repo Info Fetcher")

    label_username = tk.Label(root, text="GitHub Username:")
    label_username.pack(padx=10, pady=5)

    entry_username = tk.Entry(root, width=30)
    entry_username.pack(padx=10, pady=5)

    btn_fetch = tk.Button(root, text="Fetch and Save", command=submit)
    btn_fetch.pack(padx=10, pady=15)

    root.mainloop()

def main():
    parser = argparse.ArgumentParser(description='Fetch GitHub repository information and save it to a CSV file.')
    parser.add_argument('--username', type=str, help='GitHub username to fetch repositories for')
    parser.add_argument('--output', type=str, default='github_repos.csv', help='Output CSV filename')

    args = parser.parse_args()

    if args.username:
        fetch_and_save_repos(args.username, args.output)
    else:
        run_gui()

if __name__ == "__main__":
    main()
