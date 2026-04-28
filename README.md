# Download GitHub Repo Information in CSV Format
(Aşağıda Türkçe açıklamayı bulabilirsiniz / Turkish description is available below)

This project is a Python tool that retrieves all repository information of a specific GitHub user and saves it into a CSV file. The repository details are fetched via the GitHub API and written to a CSV format, making it easy to access information about all repositories of a GitHub user.

It supports both a Command Line Interface (CLI) and a Graphical User Interface (GUI).

The tool supports both a Graphical User Interface (GUI) and a Command-Line Interface (CLI).

## Requirements

To run this script, you'll need the following:

- Python 3.x
- `requests` library (to fetch data from the API)
- `tkinter` (comes standard with most Python installations, used for the GUI)

You can install the `requests` library by running the following command in your terminal or command prompt:

```bash
pip install requests
```

## Usage

### Using the Command Line Interface (CLI)

1. Download or clone the project files.
2. Run the script using the following command structure:

```bash
python GitRepoInfosCSV.py --username <github_username> [--output <custom_filename.csv>]
```

**Examples:**

- Save to the default `github_repos.csv`:
  ```bash
  python GitRepoInfosCSV.py --username octocat
  ```

- Save to a custom file:
  ```bash
  python GitRepoInfosCSV.py --username octocat --output my_repos.csv
  ```

### Using the Graphical User Interface (GUI)

If you prefer a visual interface, you can run the script without any arguments:

```bash
python GitRepoInfosCSV.py
```
A window will appear where you can enter the GitHub username and optionally choose the output CSV file location.

### CLI Mode
You can also run the script directly from the command line by providing the required `--username` argument. You can optionally specify the output file using the `--output` argument.

This will open a window where you can enter the GitHub username and optionally specify the output CSV filename. Click "Verileri Çek ve Kaydet" to fetch and save the repository information.

## Interactive Notebook

The repository also includes a Jupyter Notebook (`GitRepoInfosCSV.ipynb`) designed for interactive usage. You can run the cells in the notebook to prompt for a GitHub username and utilize the core logic to fetch and save repository data.

## Output File

The CSV file will contain the following columns:

- **Repository Name** (Repo Adı): The name of the repository
- **Description** (Açıklama): The description of the repository
- **Language** (Dil): The programming language used in the repository
- **Star Count** (Yıldız Sayısı): The number of stars the repository has on GitHub
- **Fork Count** (Fork Sayısı): The number of forks of the repository
- **URL** (URL): The GitHub URL of the repository

## License

This project is licensed under the GNU License. For more details, refer to the `LICENSE` file.
