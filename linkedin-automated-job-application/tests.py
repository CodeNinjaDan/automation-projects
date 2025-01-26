from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import TimeoutException
import time
import os
from dotenv import load_dotenv

load_dotenv()

URL = os.getenv("URL")

chrome_user_data_dir = os.path.expanduser('~/.config/google-chrome')

chrome_options = webdriver.ChromeOptions()

chrome_options.add_experimental_option("detach", True)

#Open Chrome in full screen for consistent placement of web elements
chrome_options.add_argument("--start-maximized")

#Path to Chrome on Linux
chrome_options.add_argument(f"user-data-dir={chrome_user_data_dir}")

driver = webdriver.Chrome(options=chrome_options)
driver.get(URL)

follow_button = WebDriverWait(driver,15).until(
                ec.element_to_be_clickable((By.CSS_SELECTOR, 'follow   artdeco-button artdeco-button--secondary ml5'))
            )
follow_button.click()