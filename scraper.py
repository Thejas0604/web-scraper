import logging
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from selenium.common.exceptions import TimeoutException, NoSuchElementException, WebDriverException

class Scraper:
    def __init__(self, browser):
        self.browser = browser

    def search_amazon(self, keyword):
        try:
            self.browser.get('https://www.amazon.com')
            input_search = wait(self.browser, 10).until(EC.presence_of_element_located((By.ID, 'twotabsearchtextbox')))
            search_button = wait(self.browser, 10).until(EC.element_to_be_clickable((By.XPATH, "(//input[@type='submit'])[1]")))
            input_search.send_keys(keyword)
            sleep(1)
            search_button.click()
        except (TimeoutException, WebDriverException) as e:
            logging.error(f"Error during Amazon search: {e}")

    def extract_product_details(self, item):
        product = {}
        try:
            product['name'] = item.find_element(By.XPATH, './/span[@class="a-size-medium a-color-base a-text-normal"]').text
        except NoSuchElementException as e:
            logging.warning(f"Error extracting product name: {e}")
            product['name'] = 'N/A'
        
        try:
            whole_price = item.find_element(By.XPATH, './/span[@class="a-price-whole"]').text
            fraction_price = item.find_element(By.XPATH, './/span[@class="a-price-fraction"]').text
            product['price'] = f"{whole_price}.{fraction_price}"
        except NoSuchElementException as e:
            logging.warning(f"Error extracting product price: {e}")
            product['price'] = 'N/A'
        
        try:
            product['availability'] = item.find_element(By.XPATH, './/span[contains(@class, "a-declarative")]/span').text
        except NoSuchElementException as e:
            logging.warning(f"Error extracting product availability: {e}")
            product['availability'] = 'N/A'
        
        try:
            product['rating'] = item.find_element(By.XPATH, './/span[@class="a-icon-alt"]').get_attribute('innerHTML')
        except NoSuchElementException as e:
            logging.warning(f"Error extracting product rating: {e}")
            product['rating'] = 'N/A'
        
        return product

    def scrape_amazon_products(self, num_pages=10):
        products = []
        for i in range(num_pages):
            try:
                logging.info(f'Scraping page {i+1}')
                product_elements = wait(self.browser, 10).until(EC.presence_of_all_elements_located((By.XPATH, "//div[contains(@class, 's-result-item s-asin')]")))
                for item in product_elements:
                    product = self.extract_product_details(item)
                    products.append(product)
                
                try:
                    next_button = wait(self.browser, 10).until(EC.element_to_be_clickable((By.XPATH, "//a[text()='Next']")))
                    next_button.click()
                    sleep(2)
                except (TimeoutException, NoSuchElementException) as e:
                    logging.info("No more pages to scrape.")
                    break
            except (TimeoutException, WebDriverException) as e:
                logging.error(f"Error scraping page {i+1}: {e}")
                break
        return products