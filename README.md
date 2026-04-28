# Download GitHub Repo Information in CSV Format
(Aşağıda Türkçe açıklamayı bulabilirsiniz / Turkish description is available below)

This project is a simple Python script that retrieves all repository information of a specific GitHub user and saves it into a CSV file. The repository details are fetched via the API and written to a CSV format, making it easy to access information about all repositories of a GitHub user.

The tool supports both a Graphical User Interface (GUI) and a Command-Line Interface (CLI).

## Requirements

To run this script, you'll need the following:

- Python 3.x
- `requests` library (to fetch data from the API)
- `tkinter` library (usually included with Python, used for the GUI)

You can install the `requests` library by running the following command in your terminal or command prompt:

```bash
pip install requests
```

## Usage

1. Download or clone the project files.
2. Run the Python script in your preferred mode:

### GUI Mode
Simply run the script without any arguments to launch the graphical interface:

```bash
python GitRepoInfosCSV.py
```
A window will appear where you can enter the GitHub username and optionally choose the output CSV file location.

### CLI Mode
You can also run the script directly from the command line by providing the required `--username` argument. You can optionally specify the output file using the `--output` argument.

```bash
python GitRepoInfosCSV.py --username your_github_username
```
A window will open allowing you to enter the GitHub username and choose where to save the output CSV file.

### Command Line Interface (CLI)
To run the script via the command line, use the following arguments:

Example with custom output file:
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
