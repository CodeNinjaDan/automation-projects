import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
import os
from dotenv import load_dotenv

load_dotenv()


PROMISED_DOWN = 20
PROMISED_UP = 15

class InternetSpeedTwitterBot:

    def __init__(self):

        self.chrome_user_data_dir = os.path.expanduser('~/.config/google-chrome')
        self.chrome_options = webdriver.ChromeOptions()
        self.chrome_options.add_experimental_option("detach", True)
        self.chrome_options.add_argument("--start-maximized")
        self.chrome_options.add_argument(f"user-data-dir={self.chrome_user_data_dir}")
        self.driver = webdriver.Chrome(options=self.chrome_options)
        self.down = 0
        self.up = 0


    def get_internet_speed(self):
        speedtest_url = "https://www.speedtest.net/"
        self.driver.get(speedtest_url)
        speedtest = WebDriverWait(self.driver, 15).until(
                ec.element_to_be_clickable(
                    (By.CSS_SELECTOR, ".js-start-test.test-mode-multi"))
            )
        speedtest.click()

        time.sleep(100)
        down_speed = WebDriverWait(self.driver, 100).until(
        ec.presence_of_element_located((By.CSS_SELECTOR, ".result-data-large.number.result-data-value.download-speed"))
           )
        self.down = int(down_speed.text)

        up_speed = WebDriverWait(self.driver, 100).until(
            ec.presence_of_element_located(
                (By.CSS_SELECTOR, ".result-data-large.number.result-data-value.upload-speed"))
        )
        self.up = int(up_speed.text)

        return self.down and self.up




    def tweet_at_provider(self):
        xusername = os.getenv("TWITTER_USERNAME")
        xpassword = os.getenv("TWITTER_PASSWORD")

        pass


test = InternetSpeedTwitterBot()
test.get_internet_speed()