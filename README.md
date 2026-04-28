# Download GitHub Repo Information in CSV Format
(Aşağıda Türkçe açıklamayı bulabilirsiniz / Turkish description is available below)

This project is a Python script that retrieves all repository information of a specific GitHub user and saves it into a CSV file. The repository details are fetched via the GitHub API and written to a CSV format, making it easy to access information about all repositories of a GitHub user.

The script supports both a Command Line Interface (CLI) and a Graphical User Interface (GUI).

## Requirements

To run this tool, you'll need the following:

- Python 3.x
- `requests` library (to fetch data from the API)
- `tkinter` library (usually included with standard Python installations, required for the GUI)

You can install the `requests` library by running the following command in your terminal or command prompt:

```bash
pip install requests
```

## Usage

You can use the script either from the Command Line Interface (CLI) or through a Graphical User Interface (GUI).

### GUI Usage

If you run the script without any arguments, a graphical user interface will open. This allows you to easily input the username and optionally choose where to save the generated CSV file.

```bash
python GitRepoInfosCSV.py
```

1. Enter the GitHub username.
2. (Optional) Choose the output CSV file location.
3. Click "Verileri Çek ve Kaydet" to fetch and save the repository data.

### CLI Usage

You can run the script via the command line by providing arguments.

```bash
python GitRepoInfosCSV.py --username <username> [--output <filename.csv>]
```

#### Examples

Fetch repos for a user and save to the default `github_repos.csv`:
```bash
python GitRepoInfosCSV.py --username gitmuhammedalbayrak
```

Fetch repos for a user and save to a custom file:
```bash
python GitRepoInfosCSV.py --username gitmuhammedalbayrak --output my_repos.csv
```

#### Options

- `-u, --username`: The GitHub username to fetch repos for. (Required)
- `-o, --output`: The output CSV filename. (Optional, defaults to `github_repos.csv`)
- `-h, --help`: Show the help message and exit.

## Output File

The generated CSV file will contain the following columns:

- **Repo Adı (Repository Name)**: The name of the repository
- **Açıklama (Description)**: The description of the repository
- **Dil (Language)**: The programming language used in the repository
- **Yıldız Sayısı (Star Count)**: The number of stars the repository has on GitHub
- **Fork Sayısı (Fork Count)**: The number of forks of the repository
- **URL**: The GitHub URL of the repository

## Interactive Notebook

The repository also includes a Jupyter Notebook (`GitRepoInfosCSV.ipynb`) designed for interactive usage.

## License

This project is licensed under the GNU License. For more details, refer to the `LICENSE` file.
