# -*- coding: utf-8 -*-

import requests
import csv
import argparse
import sys
import tkinter as tk
from tkinter import messagebox, filedialog

def fetch_and_save_repos(username, output_file='github_repos.csv'):
    # GitHub API URL'si
    url = f"https://api.github.com/users/{username}/repos"

    # API'den verileri çek
    try:
        response = requests.get(url)
        response.raise_for_status()
        repos = response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data from GitHub API: {e}")
        return False

    # CSV dosyasına yazma
    try:
        with open(output_file, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)

            # CSV başlıkları (Turkish to maintain backward compatibility)
            writer.writerow(['Repo Adı', 'Açıklama', 'Dil', 'Yıldız Sayısı', 'Fork Sayısı', 'URL'])

            # Her repo için bilgileri yaz
            for repo in repos:
                writer.writerow([repo.get('name', ''), repo.get('description', ''), repo.get('language', ''), repo.get('stargazers_count', 0), repo.get('forks_count', 0), repo.get('html_url', '')])

        print(f"Repository information successfully written to {output_file}.")
        return True
    except Exception as e:
        print(f"Error writing to CSV file: {e}")
        return False

def run_gui():
    def fetch_repos():
        username = username_entry.get().strip()
        if not username:
            messagebox.showwarning("Input Error", "Please enter a GitHub username.")
            return

        output_file = filedialog.asksaveasfilename(
            defaultextension=".csv",
            initialfile="github_repos.csv",
            filetypes=[("CSV files", "*.csv"), ("All files", "*.*")],
            title="Save as..."
        )
        if not output_file:
            return  # User cancelled

        success = fetch_and_save_repos(username, output_file)
        if success:
            messagebox.showinfo("Success", f"Repository information successfully written to {output_file}.")
        else:
            messagebox.showerror("Error", "Failed to fetch repositories. Please check the username or your connection.")

    root = tk.Tk()
    root.title("GitHub Repo Info Fetcher")
    root.geometry("400x150")
    root.resizable(False, False)

    # Username Label
    tk.Label(root, text="GitHub Username:", font=("Arial", 10)).pack(pady=(20, 5))

    # Username Entry
    username_entry = tk.Entry(root, font=("Arial", 12), width=30)
    username_entry.pack(pady=5)

    # Fetch Button
    fetch_btn = tk.Button(root, text="Fetch and Save to CSV", font=("Arial", 10, "bold"), command=fetch_repos)
    fetch_btn.pack(pady=10)

    root.mainloop()

def main():
    parser = argparse.ArgumentParser(description="Fetch GitHub repositories and save to a CSV file.")
    parser.add_argument('--username', type=str, help="GitHub username")
    parser.add_argument('--output', type=str, default='github_repos.csv', help="Output CSV filename (default: github_repos.csv)")

    args = parser.parse_args()

    if args.username:
        # Run CLI mode
        fetch_and_save_repos(args.username, args.output)
    else:
        # Run GUI mode
        run_gui()

if __name__ == "__main__":
    main()
