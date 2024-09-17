# News Summarizer: Unlocking Valuable Data from BBC News

## Overview

This project is designed to scrape news headlines, summaries, and links from the [BBC News](https://www.bbc.com/news) website. The goal is to extract valuable information from a website that doesn't provide a publicly accessible API, demonstrating how web scraping can be utilized to gather data for educational and research purposes.

## Table of Contents

- [Purpose of Data Collection](#purpose-of-data-collection)
- [Data Source Selection](#data-source-selection)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Usage](#usage)
- [Features](#features)
- [Collection Practices](#collection-practices)
- [Data Handling and Privacy](#data-handling-and-privacy)
- [Data Usage](#data-usage)
- [Ethical Considerations](#ethical-considerations)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

## Purpose of Data Collection

The primary purpose of this project is to extract and analyze news data from BBC News to:

- Provide users with quick access to the latest news headlines and summaries.
- Enable keyword-based filtering to help users find news articles relevant to their interests.
- Demonstrate the practical application of web scraping techniques in a real-world scenario.

## Data Source Selection

- **Website Used**: [BBC News](https://www.bbc.com/news)
- **Why Chosen**: BBC News is a reputable source of global news that doesn't offer a publicly accessible API for extracting news data. Scraping this site allows us to obtain timely news information that can be valuable for analysis and research.
- **Robots.txt Compliance**: We have reviewed the BBC's [robots.txt](https://www.bbc.com/robots.txt) file and ensured that our scraping activities comply with their guidelines.

## Project Structure

```
News-Summarizer/
├── main.py
├── requirements.txt
├── README.md
├── ETHICS.md
├── .gitignore
```

- **`main.py`**: The main Python script for scraping the news data.
- **`requirements.txt`**: A list of required Python packages.
- **`README.md`**: Project documentation.
- **`ETHICS.md`**: Discussion of ethical considerations.
- **`.gitignore`**: Excludes virtual environment and other unnecessary files from the repository.

## Installation

1. **Clone the Repository**:

   ```bash
   git clone https://github.com/Muneeb-Alvi/News-Summarizer.git
   ```

2. **Navigate to the Project Directory**:

   ```bash
   cd News-Summarizer
   ```

3. **Set Up a Virtual Environment**:

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

4. **Install Required Libraries**:

   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. **Run the Script**:

   ```bash
   python main.py
   ```

2. **Enter a Keyword (Optional)**:

   - When prompted, enter a keyword to filter news articles.
   - Press **Enter** without typing anything to display all available news articles.

3. **View the Results**:

   - The script will display the news articles along with their summaries and links.

## Features

- **Scrape Latest News**: Fetches the most recent news stories from the BBC News homepage.
- **Extract Detailed Information**: Retrieves the headline, summary, and direct link for each news article.
- **Keyword Filtering**: Allows users to filter news articles by keywords in the title or summary.
- **Duplicate Prevention**: Ensures that duplicate news articles are not displayed.

## Collection Practices

- **Respect Robots.txt**: The scraper only accesses parts of the website that are not disallowed by the `robots.txt` file.
- **Rate Limiting**: The script is designed to be efficient and respectful, minimizing the number of requests to avoid overloading the server.
- **No Bypassing Restrictions**: The scraper does not attempt to access password-protected areas or bypass any security measures.

## Data Handling and Privacy

- **No Personal Data Collection**: The scraper does not collect any Personally Identifiable Information (PII) or user-specific data.
- **Secure Data Storage**: Any data collected is stored securely and is included in the `.gitignore` file to prevent accidental uploads to public repositories.

## Data Usage

- **Educational and Research Purposes Only**: The data collected is intended solely for educational demonstrations and research.
- **No Commercial Use**: The data will not be used for commercial purposes or redistributed.

## Ethical Considerations

For a detailed discussion on the ethical considerations of this project and how they are addressed, please refer to the [ETHICS.md](ETHICS.md) file.

## Contributing

Contributions are welcome! If you have suggestions for improvements or encounter any issues, please open an issue or submit a pull request.
