# -*- coding: utf-8 -*-

import requests
import csv
import argparse
import sys
import tkinter as tk
from tkinter import messagebox, filedialog

def fetch_and_save_repos(username, output_file="github_repos.csv"):
    """
    Fetches GitHub repository information for the given user and saves it to a CSV file.
    """
    url = f"https://api.github.com/users/{username}/repos"

    try:
        response = requests.get(url)
        response.raise_for_status()
        repos = response.json()
    except requests.exceptions.RequestException as e:
        return False, f"Failed to fetch data for user '{username}': {e}"

    if not repos:
        return False, f"No repositories found for user '{username}' or user does not exist."

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
        return True, f"Repo bilgileri {output_file} dosyasına yazıldı."
    except IOError as e:
        return False, f"Failed to write to file '{output_file}': {e}"

def run_gui():
    """
    Launches a tkinter GUI to input username and select output file.
    """
    def on_submit():
        username = entry_username.get().strip()
        if not username:
            messagebox.showwarning("Uyarı", "Lütfen bir GitHub kullanıcı adı girin.")
            return

        output_file = entry_output.get().strip()
        if not output_file:
            output_file = "github_repos.csv"

        success, message = fetch_and_save_repos(username, output_file)
        if success:
            messagebox.showinfo("Başarılı", message)
        else:
            messagebox.showerror("Hata", message)

    def browse_file():
        filename = filedialog.asksaveasfilename(
            defaultextension=".csv",
            filetypes=[("CSV files", "*.csv"), ("All files", "*.*")],
            initialfile="github_repos.csv",
            title="Dosyayı Kaydet"
        )
        if filename:
            entry_output.delete(0, tk.END)
            entry_output.insert(0, filename)

    root = tk.Tk()
    root.title("GitHub Repo Bilgisi İndirici")
    root.geometry("450x200")
    root.resizable(False, False)

    tk.Label(root, text="GitHub Kullanıcı Adı:").pack(pady=(15, 5))
    entry_username = tk.Entry(root, width=40)
    entry_username.pack()

    tk.Label(root, text="Çıktı Dosyası (Opsiyonel):").pack(pady=(10, 5))

    frame_output = tk.Frame(root)
    frame_output.pack()

    entry_output = tk.Entry(frame_output, width=30)
    entry_output.insert(0, "github_repos.csv")
    entry_output.pack(side=tk.LEFT, padx=(0, 5))

    btn_browse = tk.Button(frame_output, text="Gözat", command=browse_file)
    btn_browse.pack(side=tk.LEFT)

    btn_submit = tk.Button(root, text="Verileri Çek ve Kaydet", command=on_submit, bg="#4CAF50", fg="white", font=("Arial", 10, "bold"))
    btn_submit.pack(pady=20)

    root.mainloop()

def main():
    # If there are arguments, run CLI mode. Otherwise, GUI mode.
    if len(sys.argv) > 1:
        parser = argparse.ArgumentParser(description="Download GitHub Repo Information in CSV Format")
        parser.add_argument("--username", "-u", type=str, required=True, help="GitHub username to fetch repos for.")
        parser.add_argument("--output", "-o", type=str, default="github_repos.csv", help="Output CSV filename (default: github_repos.csv)")

        args = parser.parse_args()

        success, message = fetch_and_save_repos(args.username, args.output)
        if success:
            print(f"Başarılı: {message}")
        else:
            print(f"Hata: {message}", file=sys.stderr)
            sys.exit(1)
    else:
        run_gui()

if __name__ == "__main__":
    main()
