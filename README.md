# Download GitHub Repo Information in CSV Format
(Aşağıda Türkçe açıklamayı bulabilirsiniz / Turkish description is available below)

This project is a simple Python script that retrieves all repository information of a specific GitHub user and saves it into a CSV file. The repository details are fetched via the GitHub API and written to a CSV format, making it easy to access information about all repositories of a GitHub user.

The tool provides both a Command Line Interface (CLI) and a Graphical User Interface (GUI). It also includes a Jupyter Notebook for interactive usage.

## Requirements

To run this tool, you'll need the following:

- Python 3.x
- `requests` library (to fetch data from the API)
- `tkinter` (usually comes pre-installed with Python, required for the GUI)

You can install the `requests` library by running the following command in your terminal or command prompt:

```bash
pip install requests
```

## Usage

You can use the script in either GUI mode or CLI mode.

### 1. GUI Mode (Graphical User Interface)
If you run the script without any arguments, a graphical user interface will launch:
```bash
python GitRepoInfosCSV.py
```
- A window will appear prompting you to enter the GitHub username.
- Click the "Fetch and Save Repos" button.
- You will be prompted to select where to save the generated CSV file.

### 2. CLI Mode (Command Line Interface)
If you prefer the command line, you can pass arguments directly to the script:
```bash
python GitRepoInfosCSV.py --username <github_username>
```
You can also specify a custom output filename:
```bash
python GitRepoInfosCSV.py --username <github_username> --output my_custom_repos.csv
```
For more details on CLI arguments, you can use the help flag:
```bash
python GitRepoInfosCSV.py --help
```

### 3. Jupyter Notebook
The project includes a `GitRepoInfosCSV.ipynb` file for interactive use within Jupyter environments (like Jupyter Lab or Google Colab). Simply open the notebook, and it will prompt you for a username.

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
