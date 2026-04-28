# -*- coding: utf-8 -*-

import requests
import csv
import argparse

def run_gui():
    """Runs the tkinter GUI for the application."""
    import tkinter as tk
    from tkinter import messagebox, filedialog

    def on_fetch_clicked():
        username = username_entry.get().strip()
        if not username:
            messagebox.showwarning("Input Error", "Please enter a GitHub username.")
            return

        output_file = output_entry.get().strip()
        if not output_file:
            output_file = 'github_repos.csv'

        success = fetch_and_save_repos(username, output_file)
        if success:
            messagebox.showinfo("Success", f"Repository information saved to:\n{output_file}")
        else:
            messagebox.showerror("Error", "Failed to fetch or save repository information. Please check the username and try again.")

    def browse_output():
        filename = filedialog.asksaveasfilename(
            defaultextension=".csv",
            filetypes=[("CSV Files", "*.csv"), ("All Files", "*.*")],
            title="Select Output File"
        )
        if filename:
            output_entry.delete(0, tk.END)
            output_entry.insert(0, filename)

    root = tk.Tk()
    root.title("GitHub Repo Fetcher")

    # Configure padding
    frame = tk.Frame(root, padx=20, pady=20)
    frame.pack(expand=True, fill=tk.BOTH)

    # Username input
    tk.Label(frame, text="GitHub Username:").grid(row=0, column=0, sticky=tk.W, pady=(0, 10))
    username_entry = tk.Entry(frame, width=40)
    username_entry.grid(row=0, column=1, pady=(0, 10))

    # Output file input
    tk.Label(frame, text="Output File:").grid(row=1, column=0, sticky=tk.W, pady=(0, 20))
    output_entry = tk.Entry(frame, width=40)
    output_entry.insert(0, "github_repos.csv")
    output_entry.grid(row=1, column=1, pady=(0, 20))

    browse_btn = tk.Button(frame, text="Browse...", command=browse_output)
    browse_btn.grid(row=1, column=2, padx=(10, 0), pady=(0, 20))

    # Fetch button
    fetch_btn = tk.Button(frame, text="Fetch and Save", command=on_fetch_clicked, bg="#4CAF50", fg="white", font=("Arial", 10, "bold"))
    fetch_btn.grid(row=2, column=0, columnspan=3, pady=10)

    # Make the window non-resizable
    root.resizable(False, False)

    # Start the GUI event loop
    root.mainloop()

def fetch_and_save_repos(username, output_file='github_repos.csv'):
    """Fetches GitHub repositories for a given username and saves them to a CSV file."""
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

            # CSV başlıkları (Turkish headers for backward compatibility)
            writer.writerow(['Repo Adı', 'Açıklama', 'Dil', 'Yıldız Sayısı', 'Fork Sayısı', 'URL'])

            # Her repo için bilgileri yaz
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
    except IOError as e:
        print(f"Error writing to file {output_file}: {e}")
        return False

if __name__ == "__main__":
    # Setup argparse
    parser = argparse.ArgumentParser(description="Fetch GitHub repository information and save to CSV.")
    parser.add_argument('--username', type=str, help='The GitHub username to fetch repositories for.')
    parser.add_argument('--output', type=str, default='github_repos.csv', help='The output CSV filename (default: github_repos.csv).')

    args = parser.parse_args()

    if args.username:
        # User provided CLI arguments
        fetch_and_save_repos(args.username, args.output)
    else:
        # Launch GUI if no username argument provided
        run_gui()