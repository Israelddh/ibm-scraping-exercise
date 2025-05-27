```markdown

# Course: Python Project for Data Science (IBM)
### Coursera_ScrapingExercise

# Stock Analysis: Yahoo Finance & Web Scraping

## Description

This project is a practical exercise that combines extracting financial data from Yahoo Finance and additional data through web scraping to analyze the performance of different stocks.

It uses Python to obtain historical price and volume information, complemented with data scraped from a webpage listing major U.S. companies. Interactive charts are generated to facilitate visualization and comparison of stock behavior over time.

## Technologies and Libraries Used

- Python 3.x  
- `yfinance` for retrieving historical financial data  
- `pandas` for data manipulation and analysis  
- `BeautifulSoup` for web scraping  
- `plotly` for interactive charts  
- `requests` for web content fetching

## Features

- Download historical data (price and volume) for a set of stocks (S&P 500 index) within a defined date range.  
- Perform web scraping to obtain an updated list of companies and their stock symbols from a website.  
- Build a combined DataFrame with the collected data.  
- Visualize stock price and volume evolution through interactive charts.  
- Compare the behavior of different stocks for basic analysis.

## Exercise Objectives

- Practice using financial APIs to obtain real data.  
- Develop skills in web scraping for structured data extraction.  
- Perform exploratory data analysis and visualization with interactive tools.  
- Prepare a practical case to showcase technical ability in financial data analysis.

## How to Use the Project

1. Clone or download the repository.  
2. Install dependencies:  
   ```bash
   pip install yfinance pandas beautifulsoup4 requests plotly
