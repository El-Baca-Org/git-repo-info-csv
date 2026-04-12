# Download GitHub Repo Information in CSV Format

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