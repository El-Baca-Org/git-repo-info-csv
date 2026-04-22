# Download GitHub Repo Information in CSV Format

This project is a simple Python script that retrieves all repository information of a specific GitHub user and saves it into a CSV file. The repository details are fetched via the API and written to a CSV format, making it easy to access information about all repositories of a GitHub user.

The script provides both a Graphical User Interface (GUI) and a Command Line Interface (CLI).

## Requirements

To run this script, you'll need the following:

- Python 3.x
- `requests` library (to fetch data from the API)
- `tkinter` library (for the GUI, usually included with Python standard library)

You can install the `requests` library by running the following command in your terminal or command prompt:

```bash
pip install requests
```

## Usage

You can use this tool either through the GUI, the CLI, or interactively via the provided Jupyter Notebook.

**Note:** The script uses the unauthenticated GitHub API, which has a rate limit of 60 requests per hour per IP address.

### 1. Graphical User Interface (GUI)

If you run the script without any arguments, a simple GUI will open:

```bash
python GitRepoInfosCSV.py
```

- Enter the GitHub username in the text field.
- Click "Fetch & Save Repos".
- Choose where you want to save the CSV file.

### 2. Command Line Interface (CLI)

You can also use the script from the command line by providing arguments:

```bash
python GitRepoInfosCSV.py --username <github_username>
```

You can optionally specify the output filename using the `--output` flag:

```bash
python GitRepoInfosCSV.py --username <github_username> --output my_repos.csv
```

### 3. Jupyter Notebook (Interactive)

The repository includes a Jupyter Notebook (`GitRepoInfosCSV.ipynb`) designed for interactive usage.
When you run the notebook, it will prompt you to enter the GitHub username and will fetch and save the repository data accordingly.

## Output File

The CSV file will contain the following columns (headers are in Turkish):

- **Repo Adı**: The name of the repository
- **Açıklama**: The description of the repository
- **Dil**: The programming language used in the repository
- **Yıldız Sayısı**: The number of stars the repository has on GitHub
- **Fork Sayısı**: The number of forks of the repository
- **URL**: The GitHub URL of the repository

## License

This project is licensed under the GNU License. For more details, refer to the `LICENSE` file.
