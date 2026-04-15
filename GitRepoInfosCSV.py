# -*- coding: utf-8 -*-

import requests
import csv
import argparse
import sys
import tkinter as tk
from tkinter import messagebox

def fetch_and_save_repos(username, output_filename='github_repos.csv'):
    """
    Fetches GitHub repositories for a given user and saves them to a CSV file.
    """
    url = f"https://api.github.com/users/{username}/repos"

    try:
        response = requests.get(url)

        # Explicit check for 404 to provide a specific error message before raise_for_status
        if response.status_code == 404:
            raise ValueError(f"GitHub kullanıcısı '{username}' bulunamadı.")

        response.raise_for_status() # Raise HTTPError for other bad responses
        repos = response.json()

        # API should return a list of repositories if successful
        if not isinstance(repos, list):
            raise ValueError("GitHub API'den beklenmeyen bir yanıt alındı.")

        with open(output_filename, mode='w', newline='', encoding='utf-8') as file:
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

        return True, f"Repo bilgileri {output_filename} dosyasına başarıyla yazıldı."
    except requests.exceptions.RequestException as e:
        return False, f"API isteği başarısız oldu: {e}"
    except ValueError as e:
         return False, str(e)
    except Exception as e:
        return False, f"Bir hata oluştu: {e}"

def run_gui():
    """
    Launches a Tkinter graphical user interface.
    """
    def on_fetch():
        username = entry_username.get().strip()
        output_file = entry_output.get().strip()

        if not username:
            messagebox.showwarning("Uyarı", "Lütfen bir GitHub kullanıcı adı girin.")
            return

        if not output_file:
            output_file = 'github_repos.csv'

        btn_fetch.config(state=tk.DISABLED)
        status_label.config(text="Veriler çekiliyor, lütfen bekleyin...")
        root.update()

        success, message = fetch_and_save_repos(username, output_file)

        if success:
            messagebox.showinfo("Başarılı", message)
            status_label.config(text="Tamamlandı.")
        else:
            messagebox.showerror("Hata", message)
            status_label.config(text="Hata oluştu.")

        btn_fetch.config(state=tk.NORMAL)

    root = tk.Tk()
    root.title("GitHub Repo Bilgi Çekici")
    root.geometry("400x200")
    root.resizable(False, False)

    # Username
    tk.Label(root, text="GitHub Kullanıcı Adı:").pack(pady=(10, 0))
    entry_username = tk.Entry(root, width=40)
    entry_username.pack(pady=5)

    # Output file
    tk.Label(root, text="Çıktı Dosya Adı (Opsiyonel):").pack()
    entry_output = tk.Entry(root, width=40)
    entry_output.insert(0, "github_repos.csv")
    entry_output.pack(pady=5)

    # Fetch Button
    btn_fetch = tk.Button(root, text="Bilgileri Çek ve Kaydet", command=on_fetch)
    btn_fetch.pack(pady=10)

    # Status Label
    status_label = tk.Label(root, text="", fg="gray")
    status_label.pack()

    root.mainloop()

def main():
    # If arguments are provided (other than the script name itself), run CLI
    if len(sys.argv) > 1:
        parser = argparse.ArgumentParser(description="Fetch GitHub repository information for a user and save it to a CSV file.")
        parser.add_argument("--username", "-u", required=True, help="GitHub username to fetch repositories for")
        parser.add_argument("--output", "-o", default="github_repos.csv", help="Output CSV file name (default: github_repos.csv)")

        args = parser.parse_args()

        print(f"[{args.username}] kullanıcısının repoları çekiliyor...")
        success, message = fetch_and_save_repos(args.username, args.output)

        if success:
            print(f"BAŞARILI: {message}")
            sys.exit(0)
        else:
            print(f"HATA: {message}", file=sys.stderr)
            sys.exit(1)
    else:
        # Run GUI when no arguments are provided
        run_gui()

if __name__ == "__main__":
    main()
