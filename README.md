# Download GitHub Repo Information in CSV Format
(Aşağıda Türkçe açıklamayı bulabilirsiniz / Turkish description is available below)

This project is a Python tool that fetches GitHub repository information for a specific user via the GitHub API and saves it to a CSV file. The repository details are fetched via the API and written to a CSV format, making it easy to access information about all repositories of a GitHub user.

## Features
- **Command Line Interface (CLI):** Automate or quickly fetch data directly from your terminal.
- **Graphical User Interface (GUI):** A user-friendly window for those who prefer not to use the terminal.
- **Jupyter Notebook:** Included `.ipynb` notebook for interactive exploration.

## Requirements

To run this tool, you'll need the following:

- Python 3.x
- `requests` library (to fetch data from the API)
- `tkinter` library (usually included with standard Python installations, needed for the GUI)

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
Example:
```bash
python GitRepoInfosCSV.py --username torvalds --output torvalds_repos.csv
```

### 3. Jupyter Notebook
An interactive notebook is available in `GitRepoInfosCSV.ipynb`. Open it with Jupyter and run the cells. It will prompt you interactively for the GitHub username.

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

The CSV file will contain the following columns (headers are kept in Turkish for backward compatibility):

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
