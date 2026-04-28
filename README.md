# Download GitHub Repo Information in CSV Format
(Aşağıda Türkçe açıklamayı bulabilirsiniz / Turkish description is available below)

This project is a Python tool that fetches GitHub repository information for a specific user via the GitHub API and saves it to a CSV file. The repository details are fetched via the API and written to a CSV format, making it easy to access information about all repositories of a GitHub user.

## Features
- **Command Line Interface (CLI):** Automate or quickly fetch data directly from your terminal.
- **Graphical User Interface (GUI):** A user-friendly window for those who prefer not to use the terminal.
- **Jupyter Notebook:** Included `.ipynb` notebook for interactive exploration.

The script provides both a Graphical User Interface (GUI) and a Command Line Interface (CLI).

## Requirements

To run this tool, you'll need the following:

- Python 3.x
- `requests` library (to fetch data from the API)
- `tkinter` library (usually included in the Python standard library, but on some Linux distributions you might need to install it with `sudo apt install python3-tk`)

You can install the `requests` library by running the following command in your terminal or command prompt:

```bash
pip install requests
```

## Usage

1. Download or clone the project files.

### CLI Mode
You can use the command-line interface to quickly fetch repository information by specifying the `--username` argument. You can optionally specify an output file with `--output`.

```bash
python GitRepoInfosCSV.py --username torvalds --output torvalds_repos.csv
```

### GUI Mode
If you run the script without any arguments, it will launch a Graphical User Interface (GUI).

```bash
python GitRepoInfosCSV.py
```
This will open a window where you can input the GitHub username and the desired output filename, and then click a button to fetch and save the data.

### Jupyter Notebook
The project also includes a Jupyter Notebook (`GitRepoInfosCSV.ipynb`). When you run the notebook cells, you will be interactively prompted to enter a GitHub username.

## Output File

The CSV file will contain the following columns (headers are in Turkish):

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
