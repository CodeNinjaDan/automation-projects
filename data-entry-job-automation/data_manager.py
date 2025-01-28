from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
import os
from dotenv import load_dotenv

load_dotenv()

class DataHandler:
    """
    Constructor for entering the scraped house information to a Google form.
    """

    def __init__(self):
        chrome_user_data_dir = os.path.expanduser('~/.config/google-chrome')
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("detach", True)
        chrome_options.add_argument("--start-maximized")
        chrome_options.add_argument(f"user-data-dir={chrome_user_data_dir}")

        self.driver = webdriver.Chrome(options=chrome_options)
        self.google_form = os.getenv("GOOGLE_FORM_LINK")


    def enter_data(self, address, price, url):
        self.driver.get(self.google_form)

        enter_address = self.driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
        enter_address.send_keys(address)

        enter_price = self.driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
        enter_price.send_keys(price)

        house_url = self.driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
        house_url.send_keys(url)

        submit_button = self.driver.find_element(By.CSS_SELECTOR, "#mG61Hd > div.RH5hzf.RLS9Fe > div > div.ThHDze > div.DE3NNc.CekdCb > div.lRwqcd > div > span")
        submit_button.click()

test = DataHandler()
test.enter_data()