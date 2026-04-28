# -*- coding: utf-8 -*-

import requests
import csv
import argparse
import sys
import tkinter as tk
from tkinter import messagebox, filedialog

def fetch_and_save_repos(username, output_file):
    # GitHub API URL'si
    url = f"https://api.github.com/users/{username}/repos"

    # API'den verileri çek
    try:
        response = requests.get(url)
        response.raise_for_status()
        repos = response.json()
    except requests.exceptions.RequestException as e:
        print(f"Hata oluştu: {e}")
        return False

    if not isinstance(repos, list):
        print("Beklenmeyen API yanıtı. Kullanıcı adı doğru mu?")
        return False

    # CSV dosyasına yazma
    try:
        with open(output_file, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)

            # CSV başlıkları
            writer.writerow(['Repo Adı', 'Açıklama', 'Dil', 'Yıldız Sayısı', 'Fork Sayısı', 'URL'])

            # Her repo için bilgileri yaz
            for repo in repos:
                writer.writerow([repo.get('name'), repo.get('description'), repo.get('language'), repo.get('stargazers_count'), repo.get('forks_count'), repo.get('html_url')])

        print(f"Repo bilgileri {output_file} dosyasına yazıldı.")
        return True
    except Exception as e:
        print(f"Dosya yazılırken hata oluştu: {e}")
        return False

def run_gui():
    def submit():
        username = entry_username.get().strip()
        if not username:
            messagebox.showwarning("Uyarı", "Lütfen bir kullanıcı adı girin.")
            return

        output_file = entry_output.get().strip()
        if not output_file:
            output_file = "github_repos.csv"

        success = fetch_and_save_repos(username, output_file)
        if success:
            messagebox.showinfo("Başarılı", f"Repo bilgileri {output_file} dosyasına yazıldı.")
        else:
            messagebox.showerror("Hata", "Repo bilgileri alınırken veya kaydedilirken bir hata oluştu.")

    def browse_file():
        filename = filedialog.asksaveasfilename(
            defaultextension=".csv",
            filetypes=[("CSV files", "*.csv"), ("All files", "*.*")],
            title="Dosyayı Kaydet"
        )
        if filename:
            entry_output.delete(0, tk.END)
            entry_output.insert(0, filename)

    root = tk.Tk()
    root.title("GitHub Repo Bilgisi İndirici")

    # Kullanıcı Adı
    tk.Label(root, text="GitHub Kullanıcı Adı:").grid(row=0, column=0, padx=10, pady=10, sticky="e")
    entry_username = tk.Entry(root, width=30)
    entry_username.grid(row=0, column=1, padx=10, pady=10)

    # Çıktı Dosyası
    tk.Label(root, text="Çıktı Dosyası (CSV):").grid(row=1, column=0, padx=10, pady=10, sticky="e")
    entry_output = tk.Entry(root, width=30)
    entry_output.insert(0, "github_repos.csv")
    entry_output.grid(row=1, column=1, padx=10, pady=10)

    btn_browse = tk.Button(root, text="Gözat...", command=browse_file)
    btn_browse.grid(row=1, column=2, padx=10, pady=10)

    # Çalıştır Butonu
    btn_submit = tk.Button(root, text="Çalıştır", command=submit)
    btn_submit.grid(row=2, column=0, columnspan=3, pady=20)

    root.mainloop()

def main():
    if len(sys.argv) > 1:
        # Run in CLI mode
        parser = argparse.ArgumentParser(description="Download GitHub Repo Information in CSV Format")
        parser.add_argument("--username", required=True, help="GitHub kullanıcı adı")
        parser.add_argument("--output", default="github_repos.csv", help="Çıktı CSV dosyasının adı")

        args = parser.parse_args()
        fetch_and_save_repos(args.username, args.output)
    else:
        # Run in GUI mode
        run_gui()

if __name__ == "__main__":
    main()
