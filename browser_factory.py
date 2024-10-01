from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import WebDriverException

class BrowserFactory:
    @staticmethod
    def create_browser(headless=True):
        options = webdriver.ChromeOptions()
        if headless:
            options.add_argument('--headless')
        
        try:
            browser = webdriver.Chrome(options=options, service=Service(ChromeDriverManager().install()))
            browser.maximize_window()
            return browser
        except WebDriverException as e:
            print(f"An error occurred while creating the browser: {e}")
            return None