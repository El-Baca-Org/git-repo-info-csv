# Download GitHub Repo Information in CSV Format
(Aşağıda Türkçe açıklamayı bulabilirsiniz / Turkish description is available below)

This project is a Python tool that retrieves all repository information of a specific GitHub user and saves it into a CSV file. The repository details are fetched via the GitHub API and written to a CSV format, making it easy to access information about all repositories of a GitHub user.

## Requirements

To run this tool, you'll need the following:

- Python 3.x
- `requests` library (to fetch data from the API)
- `tkinter` library (standard in most Python distributions, for GUI)

You can install the `requests` library by running the following command in your terminal or command prompt:

```bash
pip install requests
```

## Usage

You can use the tool in three different ways: Graphical User Interface (GUI), Command Line Interface (CLI), or via the Jupyter Notebook.

### 1. Graphical User Interface (GUI)

To launch the graphical interface, run the script without any arguments:

```bash
python GitRepoInfosCSV.py
```

A window will appear where you can enter the GitHub username and the desired output filename. Click "Fetch and Save" to download the data.

### 2. Command Line Interface (CLI)

You can use the command line arguments to quickly fetch data without launching the GUI.

```bash
python GitRepoInfosCSV.py --username <github_username> [--output <custom_filename.csv>]
```

For example:
```bash
python GitRepoInfosCSV.py --username octocat --output octocat_repos.csv
```

### 3. Jupyter Notebook (Interactive Usage)

If you prefer an interactive notebook environment, you can use `GitRepoInfosCSV.ipynb`. Open the notebook in Jupyter or Google Colab, run the cells, and it will prompt you to enter the GitHub username.

## Output File

The CSV file will contain the following columns (headers are in Turkish for backward compatibility):

- **Repo Adı**: The name of the repository
- **Açıklama**: The description of the repository
- **Dil**: The programming language used in the repository
- **Yıldız Sayısı**: The number of stars the repository has on GitHub
- **Fork Sayısı**: The number of forks of the repository
- **URL**: The GitHub URL of the repository

## API Limits

Please note that this tool makes unauthenticated requests to the GitHub API, which is subject to a strict rate limit (60 requests per hour per IP address). If you exceed this limit, you may encounter permission errors (403 Forbidden) and will need to wait for the limit to reset.

## License

This project is licensed under the GNU License. For more details, refer to the `LICENSE` file.
