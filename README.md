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

You can use the script via a Command-Line Interface (CLI) or a Graphical User Interface (GUI).

### GUI Mode
To launch the Graphical User Interface, run the script without any arguments:

```bash
python GitRepoInfosCSV.py
```
This will open a window where you can enter the GitHub username and the desired output CSV filename.

### CLI Mode
To use the Command-Line Interface, run the script with the `--username` argument:

```bash
python GitRepoInfosCSV.py --username <github_username>
```

You can also optionally specify an output filename using the `--output` argument:

```bash
python GitRepoInfosCSV.py --username <github_username> --output my_repos.csv
```

To see all available arguments, use:
```bash
python GitRepoInfosCSV.py --help
```

4. After the script runs successfully, the corresponding CSV file will be generated in your specified output location (default: `github_repos.csv`), containing the repository information for the specified user.

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