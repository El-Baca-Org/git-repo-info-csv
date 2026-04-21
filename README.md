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

You can use the application either through the Graphical User Interface (GUI) or the Command Line Interface (CLI).

### Graphical User Interface (GUI)

To launch the GUI, simply run the script without any arguments:

```bash
python GitRepoInfosCSV.py
```

1. Enter your GitHub username in the text field.
2. Click "Fetch and Save to CSV".
3. Choose the location and filename to save the CSV file.
4. A success message will appear once the data is downloaded.

### Command Line Interface (CLI)

You can also run the script directly from the command line:

```bash
python GitRepoInfosCSV.py --username <your_github_username>
```

You can optionally specify a custom output filename using the `--output` argument:

```bash
python GitRepoInfosCSV.py --username <your_github_username> --output my_repos.csv
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