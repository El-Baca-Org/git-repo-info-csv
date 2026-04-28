# -*- coding: utf-8 -*-

import requests
import csv
import argparse
import sys
import tkinter as tk
from tkinter import messagebox

def fetch_and_save_repos(username, output_file='github_repos.csv'):
    # GitHub API URL'si
    url = f"https://api.github.com/users/{username}/repos"

    try:
        # API'den verileri çek
        response = requests.get(url)
        response.raise_for_status()  # Check for HTTP errors
        repos = response.json()

        # CSV dosyasına yazma
        with open(output_file, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)

            # CSV başlıkları
            writer.writerow(['Repo Adı', 'Açıklama', 'Dil', 'Yıldız Sayısı', 'Fork Sayısı', 'URL'])

            # Her repo için bilgileri yaz
            for repo in repos:
                writer.writerow([repo.get('name', ''), repo.get('description', ''), repo.get('language', ''), repo.get('stargazers_count', 0), repo.get('forks_count', 0), repo.get('html_url', '')])

        print(f"Repo bilgileri {output_file} dosyasına yazıldı.")
        return True, f"Repo bilgileri {output_file} dosyasına yazıldı."
    except requests.exceptions.RequestException as e:
        error_msg = f"Hata: API isteği başarısız oldu - {e}"
        print(error_msg)
        return False, error_msg

def main_gui():
    def on_fetch():
        username = entry_username.get()
        output_file = entry_output.get() or 'github_repos.csv'

        if not username:
            messagebox.showwarning("Uyarı", "Lütfen bir GitHub kullanıcı adı girin.")
            return

        success, message = fetch_and_save_repos(username, output_file)
        if success:
            messagebox.showinfo("Başarılı", message)
        else:
            messagebox.showerror("Hata", message)

    root = tk.Tk()
    root.title("GitHub Repo Bilgileri Çekici")

    tk.Label(root, text="GitHub Kullanıcı Adı:").grid(row=0, column=0, padx=10, pady=10, sticky='e')
    entry_username = tk.Entry(root, width=30)
    entry_username.grid(row=0, column=1, padx=10, pady=10)

    tk.Label(root, text="Çıktı Dosyası (Opsiyonel):").grid(row=1, column=0, padx=10, pady=10, sticky='e')
    entry_output = tk.Entry(root, width=30)
    entry_output.grid(row=1, column=1, padx=10, pady=10)
    entry_output.insert(0, "github_repos.csv")

    btn_fetch = tk.Button(root, text="Verileri Çek ve Kaydet", command=on_fetch)
    btn_fetch.grid(row=2, column=0, columnspan=2, pady=20)

    root.mainloop()

def main():
    parser = argparse.ArgumentParser(description="Belirtilen GitHub kullanıcısının repolarını CSV olarak kaydeder.")
    parser.add_argument("--username", help="GitHub kullanıcı adı")
    parser.add_argument("--output", default="github_repos.csv", help="Çıktı CSV dosyasının adı (varsayılan: github_repos.csv)")

    # Parse args, but only if there are arguments
    if len(sys.argv) > 1:
        args = parser.parse_args()
        if not args.username:
            print("Hata: Komut satırı kullanımında --username argümanı gereklidir.")
            sys.exit(1)
        fetch_and_save_repos(args.username, args.output)
    else:
        # Launch GUI
        main_gui()

if __name__ == "__main__":
    main()
