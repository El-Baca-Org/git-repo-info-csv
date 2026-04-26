# Download GitHub Repo Information in CSV Format

This project is a simple Python script with both a Graphical User Interface (GUI) and Command-Line Interface (CLI) that retrieves repository information for a specific GitHub user and saves it into a CSV file. The repository details are fetched via the GitHub API and written to a CSV format, making it easy to access information about all repositories of a GitHub user.

## Requirements

To run this script, you'll need the following:

- Python 3.x
- `requests` library (to fetch data from the API)
- `tkinter` library (included in standard Python installations, required for the GUI)

You can install the `requests` library by running the following command in your terminal or command prompt:

```bash
pip install requests
```

## Usage

### Using the GUI

To launch the application with a graphical interface:

```bash
python GitRepoInfosCSV.py
```

This will open a window where you can enter the GitHub username. Clicking "Fetch and Save" will generate the `github_repos.csv` file in the project folder.

### Using the CLI

To run the script directly from the command line, use the `--username` argument:

```bash
python GitRepoInfosCSV.py --username <github_username>
```

You can also specify a custom output file using the `--output` argument:

```bash
python GitRepoInfosCSV.py --username <github_username> --output my_repos.csv
```

### Using the Jupyter Notebook

For an interactive experience, open the `GitRepoInfosCSV.ipynb` notebook. Run the cells sequentially, and it will prompt you for a GitHub username during execution.

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