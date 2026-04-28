# -*- coding: utf-8 -*-

import requests
import csv
import argparse
import sys
import threading
import tkinter as tk
from tkinter import messagebox, filedialog
from tkinter import ttk

def fetch_and_save_repos(username, output_file):
    """Fetches GitHub repos for a given username and saves to a CSV file."""
    url = f"https://api.github.com/users/{username}/repos"

    try:
        response = requests.get(url)
        response.raise_for_status()
        repos = response.json()

        with open(output_file, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(['Repo Adı', 'Açıklama', 'Dil', 'Yıldız Sayısı', 'Fork Sayısı', 'URL'])

            for repo in repos:
                writer.writerow([repo.get('name', ''),
                                 repo.get('description', ''),
                                 repo.get('language', ''),
                                 repo.get('stargazers_count', 0),
                                 repo.get('forks_count', 0),
                                 repo.get('html_url', '')])
        return True, f"Repo bilgileri {output_file} dosyasına başarıyla yazıldı."
    except requests.exceptions.HTTPError as e:
        if response.status_code == 404:
            return False, f"Hata: '{username}' adında bir GitHub kullanıcısı bulunamadı."
        else:
            return False, f"HTTP Hatası: {e}"
    except requests.exceptions.RequestException as e:
        return False, f"Bağlantı Hatası: {e}"
    except Exception as e:
        return False, f"Beklenmeyen bir hata oluştu: {e}"

class GitHubRepoFetcherApp:
    def __init__(self, root):
        self.root = root
        self.root.title("GitHub Repo Bilgisi İndirici")
        self.root.geometry("450x250")
        self.root.resizable(False, False)

        style = ttk.Style()
        style.theme_use('clam')

        # Username Input
        ttk.Label(root, text="GitHub Kullanıcı Adı:").grid(row=0, column=0, padx=10, pady=15, sticky=tk.W)
        self.username_entry = ttk.Entry(root, width=30)
        self.username_entry.grid(row=0, column=1, padx=10, pady=15, sticky=tk.W)

        # Output File Input
        ttk.Label(root, text="Çıktı Dosyası (CSV):").grid(row=1, column=0, padx=10, pady=5, sticky=tk.W)
        self.output_entry = ttk.Entry(root, width=30)
        self.output_entry.insert(0, "github_repos.csv")
        self.output_entry.grid(row=1, column=1, padx=10, pady=5, sticky=tk.W)

        self.browse_button = ttk.Button(root, text="Gözat", command=self.browse_file)
        self.browse_button.grid(row=1, column=2, padx=5, pady=5)

        # Status Label
        self.status_var = tk.StringVar()
        self.status_var.set("Hazır.")
        self.status_label = ttk.Label(root, textvariable=self.status_var, foreground="blue")
        self.status_label.grid(row=2, column=0, columnspan=3, padx=10, pady=10, sticky=tk.W)

        # Fetch Button
        self.fetch_button = ttk.Button(root, text="Bilgileri İndir", command=self.start_fetch_thread)
        self.fetch_button.grid(row=3, column=1, pady=15)

    def browse_file(self):
        filename = filedialog.asksaveasfilename(
            defaultextension=".csv",
            filetypes=[("CSV files", "*.csv"), ("All files", "*.*")],
            initialfile="github_repos.csv",
            title="CSV Dosyasını Kaydet"
        )
        if filename:
            self.output_entry.delete(0, tk.END)
            self.output_entry.insert(0, filename)

    def start_fetch_thread(self):
        username = self.username_entry.get().strip()
        output_file = self.output_entry.get().strip()

        if not username:
            messagebox.showwarning("Uyarı", "Lütfen bir GitHub kullanıcı adı girin.")
            return
        if not output_file:
            messagebox.showwarning("Uyarı", "Lütfen bir çıktı dosyası adı girin.")
            return

        self.fetch_button.config(state=tk.DISABLED)
        self.status_var.set("Veriler çekiliyor, lütfen bekleyin...")
        self.root.update()

        thread = threading.Thread(target=self.fetch_repos, args=(username, output_file))
        thread.start()

    def fetch_repos(self, username, output_file):
        success, message = fetch_and_save_repos(username, output_file)

        # UI güncellemelerini ana thread'de yap
        self.root.after(0, self.handle_fetch_result, success, message)

    def handle_fetch_result(self, success, message):
        self.fetch_button.config(state=tk.NORMAL)
        if success:
            self.status_var.set("İşlem tamamlandı.")
            messagebox.showinfo("Başarılı", message)
        else:
            self.status_var.set("Hata oluştu.")
            messagebox.showerror("Hata", message)

def run_gui():
    root = tk.Tk()
    app = GitHubRepoFetcherApp(root)
    root.mainloop()

def main():
    parser = argparse.ArgumentParser(description="Belirli bir GitHub kullanıcısının repo bilgilerini CSV olarak indirir.")
    parser.add_argument("--username", type=str, help="GitHub kullanıcı adı")
    parser.add_argument("--output", type=str, default="github_repos.csv", help="Çıktı alınacak CSV dosyasının adı (varsayılan: github_repos.csv)")

    # Argümanlar verilmişse CLI modunda çalış, aksi takdirde GUI'yi aç
    if len(sys.argv) > 1:
        args = parser.parse_args()
        if not args.username:
            print("Hata: CLI modunda --username argümanı gereklidir.")
            parser.print_help()
            sys.exit(1)

        print(f"'{args.username}' kullanıcısı için veriler çekiliyor...")
        success, message = fetch_and_save_repos(args.username, args.output)
        if success:
            print(message)
        else:
            print(message)
            sys.exit(1)
    else:
        run_gui()

if __name__ == "__main__":
    main()

def main():
    parser = argparse.ArgumentParser(description="Fetch GitHub repositories for a specific user and save them to a CSV file.")
    parser.add_argument("--username", "-u", required=True, help="GitHub username")
    parser.add_argument("--output", "-o", default="github_repos.csv", help="Output CSV file name (default: github_repos.csv)")

    args = parser.parse_args()
    username = args.username
    output_file = args.output

    # GitHub API URL'si
    url = f"https://api.github.com/users/{username}/repos"

    # API'den verileri çek
    try:
        response = requests.get(url)
        response.raise_for_status() # Check for HTTP errors
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data from GitHub API: {e}", file=sys.stderr)
        sys.exit(1)

    repos = response.json()

    # Eğer kullanıcı bulunamazsa (veya repo yoksa)
    if not isinstance(repos, list):
         if isinstance(repos, dict) and repos.get('message') == 'Not Found':
              print(f"User '{username}' not found on GitHub.", file=sys.stderr)
         else:
              print(f"Unexpected response from API.", file=sys.stderr)
         sys.exit(1)

    # CSV dosyasına yazma
    try:
        with open(output_file, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)

            # CSV başlıkları
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
        print(f"Repo bilgileri {output_file} dosyasına başarıyla yazıldı.")
    except IOError as e:
        print(f"Error writing to file {output_file}: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()
