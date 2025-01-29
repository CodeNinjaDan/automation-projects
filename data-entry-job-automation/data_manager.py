from selenium import webdriver
from selenium.webdriver.common.by import By
import os
from dotenv import load_dotenv

load_dotenv()

class DataHandler:
    """
    Constructor for entering the scraped house information to a Google form.
    """

    def __init__(self):
        try:
            chrome_user_data_dir = os.path.expanduser('~/.config/google-chrome')
            chrome_options = webdriver.ChromeOptions()
            chrome_options.add_experimental_option("detach", True)
            chrome_options.add_argument("--start-maximized")
            chrome_options.add_argument(f"user-data-dir={chrome_user_data_dir}")

            self.driver = webdriver.Chrome(options=chrome_options)
            self.google_form = os.getenv("GOOGLE_FORM_LINK")

        except Exception as e:
            print(f"Error initializing the WebDriver: {e}")


    def enter_data(self, address, price, url):
        if self.driver is None:
            print("WebDriver not initialized.")
            return
        try:
            self.driver.get(self.google_form)

            enter_address = self.driver.find_element(By.CSS_SELECTOR, "#mG61Hd > div.RH5hzf.RLS9Fe > div > div.o3Dpx > div:nth-child(1) > div > div > div.AgroKb > div > div.aCsJod.oJeWuf > div > div.Xb9hP > input")
            enter_address.send_keys(address)

            enter_price = self.driver.find_element(By.CSS_SELECTOR, "#mG61Hd > div.RH5hzf.RLS9Fe > div > div.o3Dpx > div:nth-child(2) > div > div > div.AgroKb > div > div.aCsJod.oJeWuf > div > div.Xb9hP > input")
            enter_price.send_keys(price)

            house_url = self.driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
            house_url.send_keys(url)

            submit_button = self.driver.find_element(By.CSS_SELECTOR, "#mG61Hd > div.RH5hzf.RLS9Fe > div > div.ThHDze > div.DE3NNc.CekdCb > div.lRwqcd > div > span")
            submit_button.click()

        except Exception as e:
            print(f"Error entering data: {e}")
