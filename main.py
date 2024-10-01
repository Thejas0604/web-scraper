import logging
from browser_factory import BrowserFactory
from scraper import Scraper
from utils import save_to_csv, save_to_html

what_to_scrape = "PS5 Games"

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def main():
    browser = BrowserFactory.create_browser(headless=True)
    scraper = Scraper(browser)
    try:
        scraper.search_amazon(what_to_scrape)
        products = scraper.scrape_amazon_products()
        save_to_csv(products)
        save_to_html(products)
    finally:
        browser.quit()

if __name__ == "__main__":
    main()