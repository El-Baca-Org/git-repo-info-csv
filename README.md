# Download GitHub Repo Information in CSV Format
(Aşağıda Türkçe açıklamayı bulabilirsiniz / Turkish description is available below)

This project is a simple Python script with both a Graphical User Interface (GUI) and Command-Line Interface (CLI) that retrieves repository information for a specific GitHub user and saves it into a CSV file. The repository details are fetched via the GitHub API and written to a CSV format, making it easy to access information about all repositories of a GitHub user.

## Requirements

To run this tool, you'll need the following:

- Python 3.x
- `requests` library (to fetch data from the API)
- `tkinter` library (included in standard Python installations, required for the GUI)

You can install the `requests` library by running the following command in your terminal or command prompt:

```bash
pip install requests
```

## Usage

1. Download or clone the project files.
2. Run the Python script.

### Graphical User Interface (GUI)

To open the interactive Graphical User Interface, simply run the script without any arguments:

```bash
python GitRepoInfosCSV.py
```

This will open a window where you can enter the GitHub username and select the output CSV filename.

### Command Line Interface (CLI)

You can also run the script directly from the command line by providing arguments:

```bash
python GitRepoInfosCSV.py --username <github_username> [--output <filename.csv>]
```

Example:
```bash
python GitRepoInfosCSV.py --username octocat --output octocat_repos.csv
```

After the script runs, a CSV file will be generated containing the repository information for the specified user.

## Output File

The CSV file will contain the following columns (headers are in Turkish):

- **Repo Adı**: The name of the repository
- **Açıklama**: The description of the repository
- **Dil**: The programming language used in the repository
- **Yıldız Sayısı**: The number of stars the repository has on GitHub
- **Fork Sayısı**: The number of forks of the repository
- **URL**: The GitHub URL of the repository

Note: The column headers in the CSV file are in Turkish to maintain backward compatibility, while the script interface and documentation are in English.

## Rate Limits
Note that this tool makes unauthenticated requests to the GitHub API, which limits you to 60 requests per hour. If you exceed this limit, you may encounter an error (such as a 403 error) and will need to wait for the limit to reset.

## License

This project is licensed under the GNU License. For more details, refer to the `LICENSE` file.
