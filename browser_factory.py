from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class BrowserFactory:
    @staticmethod
    def create_browser(headless=True):
        options = webdriver.ChromeOptions()
        if headless:
            options.add_argument('--headless')
        browser = webdriver.Chrome(options=options, service=Service(ChromeDriverManager().install()))
        browser.maximize_window()
        return browser