# Download GitHub Repo Information in CSV Format

This project is a Python tool that retrieves all repository information of a specific GitHub user and saves it into a CSV file. The script features both a Command Line Interface (CLI) and a Graphical User Interface (GUI) for ease of use.

## Requirements

To run this script, you'll need the following:

- Python 3.x
- `requests` library
- `tkinter` (usually comes pre-installed with Python, but might need separate installation on some Linux distributions)

You can install the `requests` library by running the following command in your terminal or command prompt:

```bash
pip install requests
```

## Usage

You can use this tool either through the terminal (CLI) or with a user-friendly graphical interface (GUI).

### Graphical User Interface (GUI)

If you run the script without any arguments, it will launch the GUI:

```bash
python GitRepoInfosCSV.py
```

A window will appear where you can enter the GitHub username and the desired output CSV filename.

### Command Line Interface (CLI)

You can use command line arguments to quickly fetch and save the data without the GUI:

```bash
python GitRepoInfosCSV.py --username <github_username> [--output <filename.csv>]
```

**Example:**

```bash
python GitRepoInfosCSV.py --username torvalds --output torvalds_repos.csv
```

If you don't specify the `--output` argument, the data will be saved to `github_repos.csv` by default.

### Interactive Notebook

The repository also includes a Jupyter Notebook (`GitRepoInfosCSV.ipynb`). When run, it will interactively prompt you for a GitHub username and generate the CSV file.

## Output File

The output CSV file will have Turkish headers for backward compatibility. The columns are:

- **Repo Adı**: The name of the repository
- **Açıklama**: The description of the repository
- **Dil**: The programming language used in the repository
- **Yıldız Sayısı**: The number of stars the repository has on GitHub
- **Fork Sayısı**: The number of forks of the repository
- **URL**: The GitHub URL of the repository

## Rate Limiting

This script makes unauthenticated requests to the GitHub API, which is subject to a rate limit of 60 requests per hour. If you encounter a 403 error, you may have exceeded this limit and will need to wait for it to reset.

## License

This project is licensed under the GNU License. For more details, refer to the `LICENSE` file.
