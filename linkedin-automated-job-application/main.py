import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import os
from dotenv import load_dotenv

load_dotenv()

URL = os.getenv("URL")
linkedin_user = os.getenv("LINKEDIN_USERNAME")
linkedin_pass = os.getenv("LINKEDIN_PASSWORD")


chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
chrome_options.add_argument("--start-maximized")

driver = webdriver.Chrome(options=chrome_options)
driver.get(URL)

sign_in = driver.find_element(By.XPATH, value='//*[@id="base-contextual-sign-in-modal"]/div/section/div/div/div/div[2]/button')
#Wait for page to load
time.sleep(7)
sign_in.click()

enter_username = driver.find_element(By.ID, value="base-sign-in-modal_session_key")
time.sleep(3)
enter_username.send_keys(linkedin_user)

enter_password = driver.find_element(By.ID, value="base-sign-in-modal_session_password")
enter_password.send_keys(linkedin_pass)

enter_logins = driver.find_element(By.XPATH, value='//*[@id="base-sign-in-modal"]/div/section/div/div/form/div[2]/button')
enter_logins.click()
