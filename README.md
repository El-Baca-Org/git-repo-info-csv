# Download GitHub Repo Information in CSV Format

This project is a simple Python tool that retrieves repository information of a specific GitHub user via the GitHub API and saves it into a CSV file. It provides an easy way to export and analyze repository details for any user.

The project supports three different ways of usage: a Graphical User Interface (GUI), a Command Line Interface (CLI), and an interactive Jupyter Notebook.

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

### 1. Graphical User Interface (GUI)

The easiest way to use the script is via its graphical interface. If you run the script without any arguments, a simple window will appear:

```bash
python GitRepoInfosCSV.py
```

- Enter the target **GitHub Username**.
- (Optional) Provide a custom **Output File Name** (defaults to `github_repos.csv`).
- Click the button to fetch and save the repository information.

### 2. Command Line Interface (CLI)

For automation or quick terminal usage, you can pass arguments directly to the script:

```bash
# Basic usage (outputs to github_repos.csv)
python GitRepoInfosCSV.py --username torvalds

# Advanced usage (specify custom output file)
python GitRepoInfosCSV.py --username torvalds --output linus_repos.csv
```

To see all available options, run: `python GitRepoInfosCSV.py --help`

### 3. Jupyter Notebook

For an interactive, step-by-step experience, you can use the provided Jupyter Notebook:

1. Open `GitRepoInfosCSV.ipynb` in Jupyter Notebook or Google Colab.
2. Run the cells sequentially.
3. When prompted, type the GitHub username.
4. The notebook will fetch the data and save it as `github_repos.csv` in the current working directory.

## Output File

The generated CSV file will contain the following columns:

- **Repo Adı (Repository Name)**: The name of the repository
- **Açıklama (Description)**: The description of the repository
- **Dil (Language)**: The primary programming language used in the repository
- **Yıldız Sayısı (Star Count)**: The number of stars the repository has on GitHub
- **Fork Sayısı (Fork Count)**: The number of forks of the repository
- **URL**: The GitHub URL of the repository

## License

This project is licensed under the GNU License. For more details, refer to the `LICENSE` file.