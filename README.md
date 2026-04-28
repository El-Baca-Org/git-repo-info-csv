# Download GitHub Repo Information in CSV Format
(Aşağıda Türkçe açıklamayı bulabilirsiniz / Turkish description is available below)

This project is a simple Python script with both a Graphical User Interface (GUI) and Command-Line Interface (CLI) that retrieves repository information for a specific GitHub user and saves it into a CSV file. The repository details are fetched via the GitHub API and written to a CSV format, making it easy to access information about all repositories of a GitHub user.

## Requirements

To run this tool, you'll need the following:

- Python 3.x
- `requests` library (to fetch data from the API)
- `tkinter` library (included in standard Python installations, required for the GUI)

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
