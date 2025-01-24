from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException
import os
from dotenv import load_dotenv

load_dotenv()

URL = os.getenv("URL")
linkedin_user = os.getenv("LINKEDIN_USERNAME")
linkedin_pass = os.getenv("LINKEDIN_PASSWORD")

#Use the current Chrome session to prevent blocking by sites
chrome_user_data_dir = os.path.expanduser('~/.config/google-chrome')

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
chrome_options.add_argument("--start-maximized")
chrome_options.add_argument(f"user-data-dir={chrome_user_data_dir}")


driver = webdriver.Chrome(options=chrome_options)
driver.get(URL)

save_button='//*[@id="main"]/div/div[2]/div[2]/div/div[2]/div/div/div[1]/div/div[1]/div/div[1]/div/div[5]/div/button'

try:
    # Sign In Button (Contextual Modal)
    sign_in = WebDriverWait(driver, 10).until(
        ec.element_to_be_clickable((By.XPATH, '//*[@id="base-contextual-sign-in-modal"]/div/section/div/div/div/div[2]/button'))
    )
    sign_in.click()

    # Username Input
    enter_username = WebDriverWait(driver, 10).until(
        ec.presence_of_element_located((By.ID, "base-sign-in-modal_session_key"))
    )
    enter_username.send_keys(linkedin_user)

    # Password Input
    enter_password = WebDriverWait(driver, 10).until(
        ec.presence_of_element_located((By.ID, "base-sign-in-modal_session_password"))
    )
    enter_password.send_keys(linkedin_pass)

    # Login Submit Button
    enter_logins = WebDriverWait(driver, 10).until(
        ec.element_to_be_clickable((By.XPATH, '//*[@id="base-sign-in-modal"]/div/section/div/div/form/div[2]/button'))
    )
    enter_logins.click()

    # Save Job Button (Link Text)
    save_jobs = WebDriverWait(driver, 10).until(
        ec.presence_of_all_elements_located((By.XPATH, '//*[@id="main"]/div/div[2]/div[2]/div/div[2]/div/div/div[1]/div/div[1]/div/div[1]/div/div[5]/div/button'))
    )
    for save in save_jobs:
        save.click()

except TimeoutException:
    print("Element not found within the specified time.")
except Exception as e:
    print(f"An error occurred: {e}")

finally:
    driver.quit()


