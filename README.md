# Download GitHub Repo Information in CSV Format
(Aşağıda Türkçe açıklamayı bulabilirsiniz / Turkish description is available below)

This project is a simple Python script that retrieves all repository information of a specific GitHub user and saves it into a CSV file. The repository details are fetched via the API and written to a CSV format, making it easy to access information about all repositories of a GitHub user.

It includes both a command-line interface (CLI) and a graphical user interface (GUI) for ease of use.

## Requirements

To run this script, you'll need the following:

- Python 3.x
- `requests` library (to fetch data from the API)
- `tkinter` library (usually included with standard Python installations, used for the GUI)

You can install the `requests` library by running the following command in your terminal or command prompt:

```bash
pip install requests
```

## Usage

1. Download or clone the project files.

### Graphical User Interface (GUI)
To use the graphical interface, run the script without any arguments:

```bash
python GitRepoInfosCSV.py
2. Run the Python script with the required `--username` argument:

```bash
python GitRepoInfosCSV.py --username your_github_username
```
A window will open allowing you to enter the GitHub username and choose where to save the output CSV file.

### Command Line Interface (CLI)
To run the script via the command line, use the following arguments:

```bash
python GitRepoInfosCSV.py --username <GitHub_Username> [--output <Filename.csv>]
```

**Options:**
- `--username`: (Required) The GitHub username whose repositories you want to download.
- `--output`: (Optional) The name of the output CSV file. Defaults to `github_repos.csv`.

**Example:**
```bash
python GitRepoInfosCSV.py --username torvalds --output linus_repos.csv
```
You can also specify a custom output file using the `--output` argument:

```bash
python GitRepoInfosCSV.py --username your_github_username --output my_repos.csv
```

3. After the script runs, a CSV file will be generated in the project folder, containing the repository information for the specified user.

## Output File

The CSV file will contain the following columns:

- **Repository Name**: The name of the repository
- **Description**: The description of the repository
- **Language**: The programming language used in the repository
- **Star Count**: The number of stars the repository has on GitHub
- **Fork Count**: The number of forks of the repository
- **URL**: The GitHub URL of the repository

## License

This project is licensed under the GNU License. For more details, refer to the `LICENSE` file.

---

# GitHub Repo Bilgilerini CSV Formatında İndir

Bu proje, belirli bir GitHub kullanıcısının tüm depo (repository) bilgilerini çeken ve bir CSV dosyasına kaydeden basit bir Python betiğidir. Depo detayları API aracılığıyla çekilir ve CSV formatında yazılır, böylece bir GitHub kullanıcısının tüm depoları hakkındaki bilgilere erişmek kolaylaşır.

## Gereksinimler

Bu betiği çalıştırmak için aşağıdakilere ihtiyacınız olacak:

- Python 3.x
- `requests` kütüphanesi (API'den veri çekmek için)

Terminal veya komut isteminizde aşağıdaki komutu çalıştırarak `requests` kütüphanesini kurabilirsiniz:

```bash
pip install requests
```

## Kullanım

1. Proje dosyalarını indirin veya klonlayın.
2. Gerekli `--username` argümanı ile Python betiğini çalıştırın:

```bash
python GitRepoInfosCSV.py --username github_kullanici_adiniz
```

Ayrıca `--output` argümanını kullanarak özel bir çıktı dosyası da belirleyebilirsiniz:

```bash
python GitRepoInfosCSV.py --username github_kullanici_adiniz --output depolarim.csv
```

3. Betik çalıştıktan sonra, proje klasöründe belirtilen kullanıcıya ait depo bilgilerini içeren bir CSV dosyası oluşturulacaktır.

## Çıktı Dosyası

CSV dosyası aşağıdaki sütunları içerecektir:

- **Repository Name**: Deponun adı
- **Description**: Deponun açıklaması
- **Language**: Depoda kullanılan programlama dili
- **Star Count**: Deponun GitHub'da sahip olduğu yıldız sayısı
- **Fork Count**: Deponun fork (çatallama) sayısı
- **URL**: Deponun GitHub URL'si

## Lisans

Bu proje GNU Lisansı altında lisanslanmıştır. Daha fazla detay için `LICENSE` dosyasına başvurabilirsiniz.