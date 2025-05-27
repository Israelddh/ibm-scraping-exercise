# Course: Python Project for Data Science (IBM)  
### Coursera_ScrapingExercise

## Stock Analysis: Yahoo Finance & Web Scraping

### Description

This project is a practical exercise from the IBM Data Science Professional Certificate on Coursera. It demonstrates how to combine financial data retrieval via the Yahoo Finance API with web scraping techniques to analyze stock performance.

The script automatically fetches a list of major U.S. companies and their stock symbols from a webpage, then downloads historical stock price and volume data using the `yfinance` library. Finally, it creates interactive visualizations to explore and compare stock behavior over time.

### Technologies and Libraries Used

- Python 3.x  
- `yfinance` for retrieving historical financial data  
- `pandas` for data manipulation and analysis  
- `BeautifulSoup` for web scraping  
- `requests` for web content fetching  
- `plotly` for interactive charts  

### Features

- Scrapes an up-to-date list of major U.S. companies and their ticker symbols.  
- Downloads historical stock price and volume data for these companies over a specified date range.  
- Combines data into a single DataFrame for analysis.  
- Generates interactive charts for stock price and volume visualization.  
- Facilitates comparison of stock performance for exploratory data analysis.  

### How to Run the Project

1. Clone or download this repository.  
2. Install the required dependencies:  
   ```bash
   pip install yfinance pandas beautifulsoup4 requests plotly

   ```bash
   pip install yfinance pandas beautifulsoup4 requests plotly
