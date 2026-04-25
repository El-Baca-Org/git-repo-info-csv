# Download GitHub Repo Information in CSV Format

This project is a simple Python script that retrieves all repository information of a specific GitHub user and saves it into a CSV file. The repository details are fetched via the API and written to a CSV format, making it easy to access information about all repositories of a GitHub user.

## Requirements

To run this script, you'll need the following:

- Python 3.x
- `requests` library (to fetch data from the API)

You can install the `requests` library by running the following command in your terminal or command prompt:

```bash
pip install requests
```

## Usage

1. Download or clone the project files.
2. Run the Python script. It supports both a Graphical User Interface (GUI) and a Command Line Interface (CLI).

### Using the GUI

To launch the GUI, run the script without any arguments:

```bash
python GitRepoInfosCSV.py
```

A window will appear allowing you to enter the GitHub username and choose where to save the CSV file.

### Using the CLI

To use the script directly from the terminal, use the `--username` argument:

```bash
python GitRepoInfosCSV.py --username <username>
```

You can optionally specify a custom output filename using the `--output` argument:

```bash
python GitRepoInfosCSV.py --username <username> --output my_repos.csv
```

After the script runs, the CSV file will be generated in the specified location.

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