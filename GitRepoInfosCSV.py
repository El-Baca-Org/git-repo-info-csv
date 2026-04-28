# -*- coding: utf-8 -*-

import requests
import csv
import argparse
import sys

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