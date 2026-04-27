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
2. You can use this script via the Command Line Interface (CLI) or a Graphical User Interface (GUI).

### Command Line Interface (CLI)

Run the script providing the GitHub username as an argument:

```bash
python GitRepoInfosCSV.py --username <username>
```

You can also specify a custom output filename:

```bash
python GitRepoInfosCSV.py --username <username> --output my_repos.csv
```

### Graphical User Interface (GUI)

Simply run the script without any arguments to launch the GUI:

```bash
python GitRepoInfosCSV.py
```

Enter the GitHub username and an optional output file name, then click "Fetch and Save".

3. After the script finishes, a CSV file will be generated in the project folder, containing the repository information for the specified user.

**Note:** The script makes unauthenticated requests to the GitHub API, which is subject to a rate limit of 60 requests per hour. If you encounter errors, you may need to wait for the limit to reset.

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