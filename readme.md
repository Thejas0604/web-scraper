# Amazon Product Scraper

## Overview

The Amazon Product Scraper is a Python-based tool that uses Selenium to scrape product information from Amazon. It extracts details such as product name, price, availability, and rating, and saves the data into both CSV and HTML files for easy viewing and analysis.

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Dependencies](#dependencies)

## Features

- Scrapes product information from Amazon.
- Extracts product name, price, availability, and rating.
- Saves the scraped data into a CSV file.
- Generates an HTML file to display the scraped data in a table format.
- Uses design patterns (Factory and Strategy) for better code organization and maintainability.
- Use of error handling

## Project Structure

```
├── browser_factory.py  # Contains the BrowserFactory class to initialize web driver instances.
├── scraper.py          # Implements the scraping logic using Selenium.
├── utils.py            # Utility functions for data processing and file handling.
├── main.py             # Entry point of the application; orchestrates the scraping process.
```

## Installation

1. **Clone the repository:**
    ```sh
    git clone https://github.com/Thejas0604/web-scraper.git
    cd web-scraper
    ```
2. **Create a virtual environment and activate it:**
    ```sh
    python -m venv .venv
    .\.venv\Scripts\activate
    ```
3. **Install the required packages:**
    ```sh
    pip install -r requirements.txt
    ```
## Usage
1. **Edit ``what_to_scrape`` variable in the ``main.py`` file.**
2. **Run the scraper:**
    ```sh
    python main.py
    ```
3. **View the results**
The scraped data will be saved in ``amazon_products.csv``.
An HTML file named ``amazon_products.html`` will be generated to display the data in a table format.

## Dependencies

- Python
- Selenium
- WebDriver Manager
- ChromeDriver
