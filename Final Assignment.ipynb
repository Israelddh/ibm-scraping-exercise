{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "<p style=\"text-align:center\">\n",
    "    <a href=\"https://skills.network/?utm_medium=Exinfluencer&utm_source=Exinfluencer&utm_content=000026UJ&utm_term=10006555&utm_id=NA-SkillsNetwork-Channel-SkillsNetworkCoursesIBMDeveloperSkillsNetworkPY0220ENSkillsNetwork900-2022-01-01\" target=\"_blank\">\n",
    "    <img src=\"https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/assets/logos/SN_web_lightmode.png\" width=\"200\" alt=\"Skills Network Logo\">\n",
    "    </a>\n",
    "</p>\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "<h1>Extracting and Visualizing Stock Data</h1>\n",
    "<h2>Description</h2>\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Extracting essential data from a dataset and displaying it is a necessary part of data science; therefore individuals can make correct decisions based on the data. In this assignment, you will extract some stock data, you will then display this data in a graph.\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "<h2>Table of Contents</h2>\n",
    "<div class=\"alert alert-block alert-info\" style=\"margin-top: 20px\">\n",
    "    <ul>\n",
    "        <li>Define a Function that Makes a Graph</li>\n",
    "        <li>Question 1: Use yfinance to Extract Stock Data</li>\n",
    "        <li>Question 2: Use Webscraping to Extract Tesla Revenue Data</li>\n",
    "        <li>Question 3: Use yfinance to Extract Stock Data</li>\n",
    "        <li>Question 4: Use Webscraping to Extract GME Revenue Data</li>\n",
    "        <li>Question 5: Plot Tesla Stock Graph</li>\n",
    "        <li>Question 6: Plot GameStop Stock Graph</li>\n",
    "    </ul>\n",
    "<p>\n",
    "    Estimated Time Needed: <strong>30 min</strong></p>\n",
    "</div>\n",
    "\n",
    "<hr>\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "***Note***:- If you are working Locally using anaconda, please uncomment the following code and execute it.\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "#!pip install yfinance==0.2.38\n",
    "#!pip install pandas==2.2.2\n",
    "#!pip install nbformat"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Collecting yfinance\n",
      "  Downloading yfinance-0.2.42-py2.py3-none-any.whl.metadata (11 kB)\n",
      "Collecting pandas>=1.3.0 (from yfinance)\n",
      "  Downloading pandas-2.2.2-cp311-cp311-manylinux_2_17_x86_64.manylinux2014_x86_64.whl.metadata (19 kB)\n",
      "Collecting numpy>=1.16.5 (from yfinance)\n",
      "  Downloading numpy-2.1.0-cp311-cp311-manylinux_2_17_x86_64.manylinux2014_x86_64.whl.metadata (60 kB)\n",
      "\u001b[2K     \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m60.9/60.9 kB\u001b[0m \u001b[31m6.2 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
      "\u001b[?25hRequirement already satisfied: requests>=2.31 in /opt/conda/lib/python3.11/site-packages (from yfinance) (2.31.0)\n",
      "Collecting multitasking>=0.0.7 (from yfinance)\n",
      "  Downloading multitasking-0.0.11-py3-none-any.whl.metadata (5.5 kB)\n",
      "Collecting lxml>=4.9.1 (from yfinance)\n",
      "  Downloading lxml-5.3.0-cp311-cp311-manylinux_2_28_x86_64.whl.metadata (3.8 kB)\n",
      "Requirement already satisfied: platformdirs>=2.0.0 in /opt/conda/lib/python3.11/site-packages (from yfinance) (4.2.1)\n",
      "Requirement already satisfied: pytz>=2022.5 in /opt/conda/lib/python3.11/site-packages (from yfinance) (2024.1)\n",
      "Collecting frozendict>=2.3.4 (from yfinance)\n",
      "  Downloading frozendict-2.4.4-py311-none-any.whl.metadata (23 kB)\n",
      "Collecting peewee>=3.16.2 (from yfinance)\n",
      "  Downloading peewee-3.17.6.tar.gz (3.0 MB)\n",
      "\u001b[2K     \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m3.0/3.0 MB\u001b[0m \u001b[31m77.8 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m:00:01\u001b[0m\n",
      "\u001b[?25h  Installing build dependencies ... \u001b[?25ldone\n",
      "\u001b[?25h  Getting requirements to build wheel ... \u001b[?25ldone\n",
      "\u001b[?25h  Preparing metadata (pyproject.toml) ... \u001b[?25ldone\n",
      "\u001b[?25hRequirement already satisfied: beautifulsoup4>=4.11.1 in /opt/conda/lib/python3.11/site-packages (from yfinance) (4.12.3)\n",
      "Collecting html5lib>=1.1 (from yfinance)\n",
      "  Downloading html5lib-1.1-py2.py3-none-any.whl.metadata (16 kB)\n",
      "Requirement already satisfied: soupsieve>1.2 in /opt/conda/lib/python3.11/site-packages (from beautifulsoup4>=4.11.1->yfinance) (2.5)\n",
      "Requirement already satisfied: six>=1.9 in /opt/conda/lib/python3.11/site-packages (from html5lib>=1.1->yfinance) (1.16.0)\n",
      "Requirement already satisfied: webencodings in /opt/conda/lib/python3.11/site-packages (from html5lib>=1.1->yfinance) (0.5.1)\n",
      "Requirement already satisfied: python-dateutil>=2.8.2 in /opt/conda/lib/python3.11/site-packages (from pandas>=1.3.0->yfinance) (2.9.0)\n",
      "Collecting tzdata>=2022.7 (from pandas>=1.3.0->yfinance)\n",
      "  Downloading tzdata-2024.1-py2.py3-none-any.whl.metadata (1.4 kB)\n",
      "Requirement already satisfied: charset-normalizer<4,>=2 in /opt/conda/lib/python3.11/site-packages (from requests>=2.31->yfinance) (3.3.2)\n",
      "Requirement already satisfied: idna<4,>=2.5 in /opt/conda/lib/python3.11/site-packages (from requests>=2.31->yfinance) (3.7)\n",
      "Requirement already satisfied: urllib3<3,>=1.21.1 in /opt/conda/lib/python3.11/site-packages (from requests>=2.31->yfinance) (2.2.1)\n",
      "Requirement already satisfied: certifi>=2017.4.17 in /opt/conda/lib/python3.11/site-packages (from requests>=2.31->yfinance) (2024.6.2)\n",
      "Downloading yfinance-0.2.42-py2.py3-none-any.whl (84 kB)\n",
      "\u001b[2K   \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m84.5/84.5 kB\u001b[0m \u001b[31m10.8 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
      "\u001b[?25hDownloading frozendict-2.4.4-py311-none-any.whl (16 kB)\n",
      "Downloading html5lib-1.1-py2.py3-none-any.whl (112 kB)\n",
      "\u001b[2K   \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m112.2/112.2 kB\u001b[0m \u001b[31m14.3 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
      "\u001b[?25hDownloading lxml-5.3.0-cp311-cp311-manylinux_2_28_x86_64.whl (5.0 MB)\n",
      "\u001b[2K   \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m5.0/5.0 MB\u001b[0m \u001b[31m59.2 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m:00:01\u001b[0m\n",
      "\u001b[?25hDownloading multitasking-0.0.11-py3-none-any.whl (8.5 kB)\n",
      "Downloading numpy-2.1.0-cp311-cp311-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (16.3 MB)\n",
      "\u001b[2K   \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m16.3/16.3 MB\u001b[0m \u001b[31m79.1 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m:00:01\u001b[0m00:01\u001b[0m\n",
      "\u001b[?25hDownloading pandas-2.2.2-cp311-cp311-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (13.0 MB)\n",
      "\u001b[2K   \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m13.0/13.0 MB\u001b[0m \u001b[31m104.7 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m00:01\u001b[0m0:01\u001b[0m\n",
      "\u001b[?25hDownloading tzdata-2024.1-py2.py3-none-any.whl (345 kB)\n",
      "\u001b[2K   \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m345.4/345.4 kB\u001b[0m \u001b[31m33.9 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
      "\u001b[?25hBuilding wheels for collected packages: peewee\n",
      "  Building wheel for peewee (pyproject.toml) ... \u001b[?25ldone\n",
      "\u001b[?25h  Created wheel for peewee: filename=peewee-3.17.6-py3-none-any.whl size=138892 sha256=778807eb7e8f76cd02aff28fbe90fcf4215c5b99c8500f3b79ee746d119ba4d6\n",
      "  Stored in directory: /home/jupyterlab/.cache/pip/wheels/1c/09/7e/9f659fde248ecdc1722a142c1d744271aad3914a0afc191058\n",
      "Successfully built peewee\n",
      "Installing collected packages: peewee, multitasking, tzdata, numpy, lxml, html5lib, frozendict, pandas, yfinance\n",
      "Successfully installed frozendict-2.4.4 html5lib-1.1 lxml-5.3.0 multitasking-0.0.11 numpy-2.1.0 pandas-2.2.2 peewee-3.17.6 tzdata-2024.1 yfinance-0.2.42\n",
      "Collecting bs4\n",
      "  Downloading bs4-0.0.2-py2.py3-none-any.whl.metadata (411 bytes)\n",
      "Requirement already satisfied: beautifulsoup4 in /opt/conda/lib/python3.11/site-packages (from bs4) (4.12.3)\n",
      "Requirement already satisfied: soupsieve>1.2 in /opt/conda/lib/python3.11/site-packages (from beautifulsoup4->bs4) (2.5)\n",
      "Downloading bs4-0.0.2-py2.py3-none-any.whl (1.2 kB)\n",
      "Installing collected packages: bs4\n",
      "Successfully installed bs4-0.0.2\n",
      "Requirement already satisfied: nbformat in /opt/conda/lib/python3.11/site-packages (5.10.4)\n",
      "Requirement already satisfied: fastjsonschema>=2.15 in /opt/conda/lib/python3.11/site-packages (from nbformat) (2.19.1)\n",
      "Requirement already satisfied: jsonschema>=2.6 in /opt/conda/lib/python3.11/site-packages (from nbformat) (4.22.0)\n",
      "Requirement already satisfied: jupyter-core!=5.0.*,>=4.12 in /opt/conda/lib/python3.11/site-packages (from nbformat) (5.7.2)\n",
      "Requirement already satisfied: traitlets>=5.1 in /opt/conda/lib/python3.11/site-packages (from nbformat) (5.14.3)\n",
      "Requirement already satisfied: attrs>=22.2.0 in /opt/conda/lib/python3.11/site-packages (from jsonschema>=2.6->nbformat) (23.2.0)\n",
      "Requirement already satisfied: jsonschema-specifications>=2023.03.6 in /opt/conda/lib/python3.11/site-packages (from jsonschema>=2.6->nbformat) (2023.12.1)\n",
      "Requirement already satisfied: referencing>=0.28.4 in /opt/conda/lib/python3.11/site-packages (from jsonschema>=2.6->nbformat) (0.35.1)\n",
      "Requirement already satisfied: rpds-py>=0.7.1 in /opt/conda/lib/python3.11/site-packages (from jsonschema>=2.6->nbformat) (0.18.0)\n",
      "Requirement already satisfied: platformdirs>=2.5 in /opt/conda/lib/python3.11/site-packages (from jupyter-core!=5.0.*,>=4.12->nbformat) (4.2.1)\n"
     ]
    }
   ],
   "source": [
    "!pip install yfinance\n",
    "!pip install bs4\n",
    "!pip install nbformat"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {},
   "outputs": [],
   "source": [
    "import yfinance as yf\n",
    "import pandas as pd\n",
    "import requests\n",
    "from bs4 import BeautifulSoup\n",
    "import plotly.graph_objects as go\n",
    "from plotly.subplots import make_subplots"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "In Python, you can ignore warnings using the warnings module. You can use the filterwarnings function to filter or ignore specific warning messages or categories.\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {},
   "outputs": [],
   "source": [
    "import warnings\n",
    "# Ignore all warnings\n",
    "warnings.filterwarnings(\"ignore\", category=FutureWarning)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Define Graphing Function\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "In this section, we define the function `make_graph`. **You don't have to know how the function works, you should only care about the inputs. It takes a dataframe with stock data (dataframe must contain Date and Close columns), a dataframe with revenue data (dataframe must contain Date and Revenue columns), and the name of the stock.**\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "metadata": {},
   "outputs": [],
   "source": [
    "def make_graph(stock_data, revenue_data, stock):\n",
    "    fig = make_subplots(rows=2, cols=1, shared_xaxes=True, subplot_titles=(\"Historical Share Price\", \"Historical Revenue\"), vertical_spacing = .3)\n",
    "    stock_data_specific = stock_data[stock_data.Date <= '2021--06-14']\n",
    "    revenue_data_specific = revenue_data[revenue_data.Date <= '2021-04-30']\n",
    "    fig.add_trace(go.Scatter(x=pd.to_datetime(stock_data_specific.Date), y=stock_data_specific.Close.astype(\"float\"), name=\"Share Price\"), row=1, col=1)\n",
    "    fig.add_trace(go.Scatter(x=pd.to_datetime(revenue_data_specific.Date), y=revenue_data_specific.Revenue.astype(\"float\"), name=\"Revenue\"), row=2, col=1)\n",
    "    fig.update_xaxes(title_text=\"Date\", row=1, col=1)\n",
    "    fig.update_xaxes(title_text=\"Date\", row=2, col=1)\n",
    "    fig.update_yaxes(title_text=\"Price ($US)\", row=1, col=1)\n",
    "    fig.update_yaxes(title_text=\"Revenue ($US Millions)\", row=2, col=1)\n",
    "    fig.update_layout(showlegend=False,\n",
    "    height=900,\n",
    "    title=stock,\n",
    "    xaxis_rangeslider_visible=True)\n",
    "    fig.show()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Use the make_graph function that we’ve already defined. You’ll need to invoke it in questions 5 and 6 to display the graphs and create the dashboard. \n",
    "> **Note: You don’t need to redefine the function for plotting graphs anywhere else in this notebook; just use the existing function.**\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Question 1: Use yfinance to Extract Stock Data\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Using the `Ticker` function enter the ticker symbol of the stock we want to extract data on to create a ticker object. The stock is Tesla and its ticker symbol is `TSLA`.\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "metadata": {},
   "outputs": [],
   "source": [
    "tesla = yf.Ticker(\"TSLA\")"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Using the ticker object and the function `history` extract stock information and save it in a dataframe named `tesla_data`. Set the `period` parameter to ` \"max\" ` so we get information for the maximum amount of time.\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "metadata": {
    "scrolled": true
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "                               Open      High       Low     Close     Volume  \\\n",
      "Date                                                                           \n",
      "2010-06-29 00:00:00-04:00  1.266667  1.666667  1.169333  1.592667  281494500   \n",
      "2010-06-30 00:00:00-04:00  1.719333  2.028000  1.553333  1.588667  257806500   \n",
      "2010-07-01 00:00:00-04:00  1.666667  1.728000  1.351333  1.464000  123282000   \n",
      "2010-07-02 00:00:00-04:00  1.533333  1.540000  1.247333  1.280000   77097000   \n",
      "2010-07-06 00:00:00-04:00  1.333333  1.333333  1.055333  1.074000  103003500   \n",
      "\n",
      "                           Dividends  Stock Splits  \n",
      "Date                                                \n",
      "2010-06-29 00:00:00-04:00        0.0           0.0  \n",
      "2010-06-30 00:00:00-04:00        0.0           0.0  \n",
      "2010-07-01 00:00:00-04:00        0.0           0.0  \n",
      "2010-07-02 00:00:00-04:00        0.0           0.0  \n",
      "2010-07-06 00:00:00-04:00        0.0           0.0  \n",
      "<class 'pandas.core.frame.DataFrame'>\n"
     ]
    }
   ],
   "source": [
    "tesla_data = tesla.history(period=\"max\")\n",
    "print(tesla_data.head())\n",
    "print(type(tesla_data))"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "**Reset the index** using the `reset_index(inplace=True)` function on the tesla_data DataFrame and display the first five rows of the `tesla_data` dataframe using the `head` function. Take a screenshot of the results and code from the beginning of Question 1 to the results below.\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "                       Date      Open      High       Low     Close  \\\n",
      "0 2010-06-29 00:00:00-04:00  1.266667  1.666667  1.169333  1.592667   \n",
      "1 2010-06-30 00:00:00-04:00  1.719333  2.028000  1.553333  1.588667   \n",
      "2 2010-07-01 00:00:00-04:00  1.666667  1.728000  1.351333  1.464000   \n",
      "3 2010-07-02 00:00:00-04:00  1.533333  1.540000  1.247333  1.280000   \n",
      "4 2010-07-06 00:00:00-04:00  1.333333  1.333333  1.055333  1.074000   \n",
      "\n",
      "      Volume  Dividends  Stock Splits  \n",
      "0  281494500        0.0           0.0  \n",
      "1  257806500        0.0           0.0  \n",
      "2  123282000        0.0           0.0  \n",
      "3   77097000        0.0           0.0  \n",
      "4  103003500        0.0           0.0  \n"
     ]
    }
   ],
   "source": [
    "tesla_data.reset_index(inplace=True)\n",
    "print(tesla_data.head())"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Question 2: Use Webscraping to Extract Tesla Revenue Data\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Use the `requests` library to download the webpage https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0220EN-SkillsNetwork/labs/project/revenue.htm Save the text of the response as a variable named `html_data`.\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "metadata": {},
   "outputs": [],
   "source": [
    "html_data = requests.get(\"https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0220EN-SkillsNetwork/labs/project/revenue.htm\").text"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Parse the html data using `beautiful_soup` using parser i.e `html5lib` or `html.parser`. Make sure to use the `html_data` with the content parameter as follow `html_data.content` .\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "metadata": {
    "scrolled": true
   },
   "outputs": [],
   "source": [
    "soup = BeautifulSoup(html_data, 'html.parser') "
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Using `BeautifulSoup` or the `read_html` function extract the table with `Tesla Revenue` and store it into a dataframe named `tesla_revenue`. The dataframe should have columns `Date` and `Revenue`.\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "<details><summary>Step-by-step instructions</summary>\n",
    "\n",
    "```\n",
    "\n",
    "Here are the step-by-step instructions:\n",
    "\n",
    "1. Find All Tables: Start by searching for all HTML tables on a webpage using `soup.find_all('table')`.\n",
    "2. Identify the Relevant Table: then loops through each table. If a table contains the text “Tesla Quarterly Revenue,”, select that table.\n",
    "3. Initialize a DataFrame: Create an empty Pandas DataFrame called `tesla_revenue` with columns “Date” and “Revenue.”\n",
    "4. Loop Through Rows: For each row in the relevant table, extract the data from the first and second columns (date and revenue).\n",
    "5. Clean Revenue Data: Remove dollar signs and commas from the revenue value.\n",
    "6. Add Rows to DataFrame: Create a new row in the DataFrame with the extracted date and cleaned revenue values.\n",
    "7. Repeat for All Rows: Continue this process for all rows in the table.\n",
    "\n",
    "```\n",
    "</details>\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "<details><summary>Click here if you need help locating the table</summary>\n",
    "\n",
    "```\n",
    "    \n",
    "Below is the code to isolate the table, you will now need to loop through the rows and columns like in the previous lab\n",
    "    \n",
    "soup.find_all(\"tbody\")[1]\n",
    "    \n",
    "If you want to use the read_html function the table is located at index 1\n",
    "\n",
    "We are focusing on quarterly revenue in the lab.\n",
    "> Note: Instead of using the deprecated pd.append() method, consider using pd.concat([df, pd.DataFrame], ignore_index=True).\n",
    "```\n",
    "\n",
    "</details>\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "    Date  Revenue\n",
      "0   2021  $53,823\n",
      "1   2020  $31,536\n",
      "2   2019  $24,578\n",
      "3   2018  $21,461\n",
      "4   2017  $11,759\n",
      "5   2016   $7,000\n",
      "6   2015   $4,046\n",
      "7   2014   $3,198\n",
      "8   2013   $2,013\n",
      "9   2012     $413\n",
      "10  2011     $204\n",
      "11  2010     $117\n",
      "12  2009     $112\n"
     ]
    }
   ],
   "source": [
    "tables = pd.read_html(str(soup))\n",
    "tesla_revenue = tables[0]\n",
    "tesla_revenue.columns = ['Date', 'Revenue']\n",
    "tesla_revenue.head()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Execute the following line to remove the comma and dollar sign from the `Revenue` column. \n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "metadata": {},
   "outputs": [],
   "source": [
    "tesla_revenue[\"Revenue\"] = tesla_revenue['Revenue'].str.replace(',|\\$',\"\", regex=True)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Execute the following lines to remove an null or empty strings in the Revenue column.\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "metadata": {},
   "outputs": [],
   "source": [
    "tesla_revenue.dropna(inplace=True)\n",
    "\n",
    "tesla_revenue = tesla_revenue[tesla_revenue['Revenue'] != \"\"]"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Display the last 5 row of the `tesla_revenue` dataframe using the `tail` function. Take a screenshot of the results.\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Date</th>\n",
       "      <th>Revenue</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>8</th>\n",
       "      <td>2013</td>\n",
       "      <td>2013</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>9</th>\n",
       "      <td>2012</td>\n",
       "      <td>413</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>10</th>\n",
       "      <td>2011</td>\n",
       "      <td>204</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>11</th>\n",
       "      <td>2010</td>\n",
       "      <td>117</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>12</th>\n",
       "      <td>2009</td>\n",
       "      <td>112</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "    Date Revenue\n",
       "8   2013    2013\n",
       "9   2012     413\n",
       "10  2011     204\n",
       "11  2010     117\n",
       "12  2009     112"
      ]
     },
     "execution_count": 18,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "tesla_revenue.tail(5)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Question 3: Use yfinance to Extract Stock Data\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Using the `Ticker` function enter the ticker symbol of the stock we want to extract data on to create a ticker object. The stock is GameStop and its ticker symbol is `GME`.\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "                               Open      High       Low     Close    Volume  \\\n",
      "Date                                                                          \n",
      "2002-02-13 00:00:00-05:00  1.620128  1.693350  1.603296  1.691667  76216000   \n",
      "2002-02-14 00:00:00-05:00  1.712707  1.716073  1.670626  1.683250  11021600   \n",
      "2002-02-15 00:00:00-05:00  1.683251  1.687459  1.658002  1.674834   8389600   \n",
      "2002-02-19 00:00:00-05:00  1.666418  1.666418  1.578047  1.607504   7410400   \n",
      "2002-02-20 00:00:00-05:00  1.615920  1.662210  1.603296  1.662210   6892800   \n",
      "\n",
      "                           Dividends  Stock Splits  \n",
      "Date                                                \n",
      "2002-02-13 00:00:00-05:00        0.0           0.0  \n",
      "2002-02-14 00:00:00-05:00        0.0           0.0  \n",
      "2002-02-15 00:00:00-05:00        0.0           0.0  \n",
      "2002-02-19 00:00:00-05:00        0.0           0.0  \n",
      "2002-02-20 00:00:00-05:00        0.0           0.0  \n"
     ]
    }
   ],
   "source": [
    "gme = yf.Ticker(\"GME\")"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Using the ticker object and the function `history` extract stock information and save it in a dataframe named `gme_data`. Set the `period` parameter to ` \"max\" ` so we get information for the maximum amount of time.\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "gme_data = gme.history(period = \"max\")\n",
    "gme_data.head()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "**Reset the index** using the `reset_index(inplace=True)` function on the gme_data DataFrame and display the first five rows of the `gme_data` dataframe using the `head` function. Take a screenshot of the results and code from the beginning of Question 3 to the results below.\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Date</th>\n",
       "      <th>Open</th>\n",
       "      <th>High</th>\n",
       "      <th>Low</th>\n",
       "      <th>Close</th>\n",
       "      <th>Volume</th>\n",
       "      <th>Dividends</th>\n",
       "      <th>Stock Splits</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>2002-02-13 00:00:00-05:00</td>\n",
       "      <td>1.620128</td>\n",
       "      <td>1.693350</td>\n",
       "      <td>1.603296</td>\n",
       "      <td>1.691667</td>\n",
       "      <td>76216000</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>2002-02-14 00:00:00-05:00</td>\n",
       "      <td>1.712707</td>\n",
       "      <td>1.716073</td>\n",
       "      <td>1.670626</td>\n",
       "      <td>1.683250</td>\n",
       "      <td>11021600</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>2002-02-15 00:00:00-05:00</td>\n",
       "      <td>1.683251</td>\n",
       "      <td>1.687459</td>\n",
       "      <td>1.658002</td>\n",
       "      <td>1.674834</td>\n",
       "      <td>8389600</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>2002-02-19 00:00:00-05:00</td>\n",
       "      <td>1.666418</td>\n",
       "      <td>1.666418</td>\n",
       "      <td>1.578047</td>\n",
       "      <td>1.607504</td>\n",
       "      <td>7410400</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>2002-02-20 00:00:00-05:00</td>\n",
       "      <td>1.615920</td>\n",
       "      <td>1.662210</td>\n",
       "      <td>1.603296</td>\n",
       "      <td>1.662210</td>\n",
       "      <td>6892800</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "                       Date      Open      High       Low     Close    Volume  \\\n",
       "0 2002-02-13 00:00:00-05:00  1.620128  1.693350  1.603296  1.691667  76216000   \n",
       "1 2002-02-14 00:00:00-05:00  1.712707  1.716073  1.670626  1.683250  11021600   \n",
       "2 2002-02-15 00:00:00-05:00  1.683251  1.687459  1.658002  1.674834   8389600   \n",
       "3 2002-02-19 00:00:00-05:00  1.666418  1.666418  1.578047  1.607504   7410400   \n",
       "4 2002-02-20 00:00:00-05:00  1.615920  1.662210  1.603296  1.662210   6892800   \n",
       "\n",
       "   Dividends  Stock Splits  \n",
       "0        0.0           0.0  \n",
       "1        0.0           0.0  \n",
       "2        0.0           0.0  \n",
       "3        0.0           0.0  \n",
       "4        0.0           0.0  "
      ]
     },
     "execution_count": 20,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "gme_data.reset_index(inplace=True)\n",
    "gme_data.head()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Question 4: Use Webscraping to Extract GME Revenue Data\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Use the `requests` library to download the webpage https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0220EN-SkillsNetwork/labs/project/stock.html. Save the text of the response as a variable named `html_data_2`.\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "metadata": {},
   "outputs": [],
   "source": [
    "html_data_2 = requests.get(\" https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0220EN-SkillsNetwork/labs/project/stock.html\").text"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Parse the html data using `beautiful_soup` using parser i.e `html5lib` or `html.parser`.\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 26,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "   Date Revenue\n",
      "0  2020    6466\n",
      "1  2019    8285\n",
      "2  2018    8547\n",
      "3  2017    7965\n",
      "4  2016    9364\n",
      "    Date Revenue\n",
      "11  2009    8806\n",
      "12  2008    7094\n",
      "13  2007    5319\n",
      "14  2006    3092\n",
      "15  2005    1843\n"
     ]
    }
   ],
   "source": [
    "soup = BeautifulSoup(html_data, 'html.parser')"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Using `BeautifulSoup` or the `read_html` function extract the table with `GameStop Revenue` and store it into a dataframe named `gme_revenue`. The dataframe should have columns `Date` and `Revenue`. Make sure the comma and dollar sign is removed from the `Revenue` column.\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "> **Note: Use the method similar to what you did in question 2.**  \n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "<details><summary>Click here if you need help locating the table</summary>\n",
    "\n",
    "```\n",
    "    \n",
    "Below is the code to isolate the table, you will now need to loop through the rows and columns like in the previous lab\n",
    "    \n",
    "soup.find_all(\"tbody\")[1]\n",
    "    \n",
    "If you want to use the read_html function the table is located at index 1\n",
    "\n",
    "\n",
    "```\n",
    "\n",
    "</details>\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "tables = pd.read_html(str(soup))\n",
    "gme_revenue = tables[0]\n",
    "gme_revenue.columns = ['Date', 'Revenue']\n",
    "\n",
    "gme_revenue[\"Revenue\"] = gme_revenue['Revenue'].str.replace(',|\\$',\"\", regex=True)\n",
    "gme_revenue.dropna(inplace=True)\n",
    "gme_revenue = gme_revenue[gme_revenue['Revenue'] != \"\"]\n",
    "\n",
    "gme_revenue.head()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Display the last five rows of the `gme_revenue` dataframe using the `tail` function. Take a screenshot of the results.\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 30,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Date</th>\n",
       "      <th>Revenue</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>14</th>\n",
       "      <td>2006</td>\n",
       "      <td>3092</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>15</th>\n",
       "      <td>2005</td>\n",
       "      <td>1843</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "    Date Revenue\n",
       "14  2006    3092\n",
       "15  2005    1843"
      ]
     },
     "execution_count": 30,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "gme_revenue.tail(5)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Question 5: Plot Tesla Stock Graph\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Use the `make_graph` function to graph the Tesla Stock Data, also provide a title for the graph. Note the graph will only show data upto June 2021.\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "<details><summary>Hint</summary>\n",
    "\n",
    "```\n",
    "\n",
    "You just need to invoke the make_graph function with the required parameter to print the graphs.The structure to call the `make_graph` function is `make_graph(tesla_data, tesla_revenue, 'Tesla')`.\n",
    "\n",
    "```\n",
    "    \n",
    "</details>\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# make_graph(tesla_data, tesla_revenue, \"TSLA\")\n",
    "# Error !"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Question 6: Plot GameStop Stock Graph\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Use the `make_graph` function to graph the GameStop Stock Data, also provide a title for the graph. The structure to call the `make_graph` function is `make_graph(gme_data, gme_revenue, 'GameStop')`. Note the graph will only show data upto June 2021.\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "<details><summary>Hint</summary>\n",
    "\n",
    "```\n",
    "\n",
    "You just need to invoke the make_graph function with the required parameter to print the graphs.The structure to call the `make_graph` function is `make_graph(gme_data, gme_revenue, 'GameStop')`\n",
    "\n",
    "```\n",
    "    \n",
    "</details>\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# make_graph(gme_data, gme_revenue, \"GME\")\n",
    "# Error!"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "<h2>About the Authors:</h2> \n",
    "\n",
    "<a href=\"https://www.linkedin.com/in/joseph-s-50398b136/\">Joseph Santarcangelo</a> has a PhD in Electrical Engineering, his research focused on using machine learning, signal processing, and computer vision to determine how videos impact human cognition. Joseph has been working for IBM since he completed his PhD.\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## <h3 align=\"center\"> © IBM Corporation 2020. All rights reserved. <h3/>\n",
    "\n",
    "```toggle ## Change Log\n",
    "```\n",
    "```toggle | Date (YYYY-MM-DD) | Version | Changed By    | Change Description        |\n",
    "```\n",
    "```toggle | ----------------- | ------- | ------------- | ------------------------- |\n",
    "```\n",
    "```toggle | 2022-02-28        | 1.2     | Lakshmi Holla | Changed the URL of GameStop |\n",
    "```\n",
    "```toggle | 2020-11-10        | 1.1     | Malika Singla | Deleted the Optional part |\n",
    "```\n",
    "```toggle | 2020-08-27        | 1.0     | Malika Singla | Added lab to GitLab       |\n",
    "```\n"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.11.9"
  },
  "prev_pub_hash": "3eff379447b11bb93fcfe9128340484c280bbca92c51ece98405a1f05537425b"
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
