📚 Books to Scrape – Web Scraping Project

# Project Description
This project is a Python web scraping script created as part of my learning process.
The data is scraped from Books to Scrape, which is a demo website built specifically for practicing ethical web scraping.
The main goal of this project was to understand how real websites are structured and how to extract useful information using Python.

# Technologies Used
Python
Requests
BeautifulSoup
Pandas

# Data Collected
For each book, the following details were scraped:
Book title
Category
Price
Availability
Rating
Product page URL

The script is currently configured to scrape 4 pages, which results in approximately 80 books.

# How the Script Works
Sends HTTP requests to fetch web pages
Parses HTML using BeautifulSoup
Uses pagination to move through multiple pages
Visits individual book pages to extract category information
Cleans the data and saves it into a CSV file using Pandas

# Output
books_data.csv – contains the final cleaned dataset


# What I Learned
How pagination works in web scraping
Extracting data from nested web pages
Cleaning text data before analysis
Writing reusable functions in Python
Saving structured data into CSV format
