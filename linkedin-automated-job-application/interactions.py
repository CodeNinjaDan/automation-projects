#Here I am going to click on each job then save and follow the company

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

#Use the current Chrome session to prevent being blocked by sites
chrome_user_data_dir = os.path.expanduser('~/.config/google-chrome')

chrome_options = webdriver.ChromeOptions()

#Keep the browser open
chrome_options.add_experimental_option("detach", True)

#Open Chrome in full screen for consistent placement of web elements
chrome_options.add_argument("--start-maximized")

#Path to Chrome on Linux
chrome_options.add_argument(f"user-data-dir={chrome_user_data_dir}")

driver = webdriver.Chrome(options=chrome_options)
driver.get(URL)


try:
    job_results = WebDriverWait(driver, 10).until(
        ec.presence_of_all_elements_located((By.CSS_SELECTOR, ".DbiQFMuFHPKdmbUaxlfthbWfPXkiOneGMWQ"))
    )
    print(job_results)

    #Iterate through each job result
    for job in job_results:
        job.click()
        try:
            #find link or clickable element that leads to the job details page
            # job_link = WebDriverWait(driver, 15).until(
            #     ec.element_to_be_clickable((By.CSS_SELECTOR, ".full-width.artdeco-entity-lockup__title.ember-view"))
            # )
            #
            # job_link.click()
            # WebDriverWait(driver, 10).until(ec.number_of_windows_to_be(2))
            # driver.switch_to.window(driver.window_handles[1]) #Switch to new tab

            # save_button = WebDriverWait(job_link,10).until(
            #     ec.element_to_be_clickable((By.CSS_SELECTOR, ".jobs-save-button.artdeco-button.artdeco-button--secondary.artdeco-button--3"))
            # )
            # save_button = WebDriverWait(driver, 13).until(
            #     ec.element_to_be_clickable(
            #         (By.CSS_SELECTOR, ".jobs-save-button.artdeco-button.artdeco-button--secondary.artdeco-button--3"))
            # )
            save_button = driver.find_element(By.CSS_SELECTOR, ".jobs-save-button.artdeco-button.artdeco-button--secondary.artdeco-button--3")
            save_button.click()

            follow_button = WebDriverWait(driver,15).until(
                ec.element_to_be_clickable((By.XPATH, '//*[@id="main"]/div/div[2]/div[2]/div/div[2]/div/div/div[1]/div/section/section/div[1]/div[1]/button'))
            )
            follow_button.click()

        except TimeoutException:
            print("Job link not found in this card.")
        except Exception as inner_e:
            print(f"An error occured while processing a job {inner_e}")


except TimeoutException:
    print("Job results did not load within the specifies time.")
except Exception as e:
    print(f"A general error occured {e}")
# finally:
#     driver.quit()