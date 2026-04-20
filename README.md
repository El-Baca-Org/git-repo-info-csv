# Download GitHub Repo Information in CSV Format

This project is a Python tool that fetches GitHub repository information for a specific user via the GitHub API and saves it to a CSV file. The repository details are fetched via the API and written to a CSV format, making it easy to access information about all repositories of a GitHub user.

## Features
- **Command Line Interface (CLI):** Automate or quickly fetch data directly from your terminal.
- **Graphical User Interface (GUI):** A user-friendly window for those who prefer not to use the terminal.
- **Jupyter Notebook:** Included `.ipynb` notebook for interactive exploration.

## Requirements

To run this script, you'll need the following:

- Python 3.x
- `requests` library (to fetch data from the API)
- `tkinter` library (usually included with standard Python installations, needed for the GUI)

You can install the `requests` library by running the following command in your terminal or command prompt:

```bash
pip install requests
```

## Usage

### 1. GUI Mode
Simply run the script without any arguments. A window will appear prompting you to enter the GitHub username and output filename.

```bash
python GitRepoInfosCSV.py
```

### 2. CLI Mode
You can specify the username and output filename directly from the command line:

```bash
python GitRepoInfosCSV.py --username <github_username> [--output custom_filename.csv]
```
Example:
```bash
python GitRepoInfosCSV.py --username torvalds --output torvalds_repos.csv
```

### 3. Jupyter Notebook
An interactive notebook is available in `GitRepoInfosCSV.ipynb`. Open it with Jupyter and run the cells. It will prompt you interactively for the GitHub username.

## Important Note regarding GitHub API Rate Limits
This script makes unauthenticated requests to the GitHub API. The API imposes a strict rate limit for unauthenticated users (currently 60 requests per hour per IP address). If you exceed this limit, the script will output an HTTP 403 error. You will need to wait for the limit to reset before making more requests.

## Output File

The CSV file will contain the following columns (headers are kept in Turkish for backward compatibility):

- **Repo Adı**: The name of the repository
- **Açıklama**: The description of the repository
- **Dil**: The programming language used in the repository
- **Yıldız Sayısı**: The number of stars the repository has on GitHub
- **Fork Sayısı**: The number of forks of the repository
- **URL**: The GitHub URL of the repository

## License

This project is licensed under the GNU License. For more details, refer to the `LICENSE` file.
