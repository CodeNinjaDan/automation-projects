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

        # Programme crashes without a waiting time.
        time.sleep(80)

        self.down = WebDriverWait(self.driver, 100).until(
        ec.presence_of_element_located((By.CSS_SELECTOR, ".result-data-large.number.result-data-value.download-speed"))
           ).text


        self.up = WebDriverWait(self.driver, 100).until(
            ec.presence_of_element_located(
                (By.CSS_SELECTOR, ".result-data-large.number.result-data-value.upload-speed"))
        ).text

        print(f"Download speed: {self.down}")
        print(f"Upload speed: {self.up}")


        # self.driver.quit()


    def tweet_at_provider(self):
        xusername = os.getenv("TWITTER_USERNAME")
        xpassword = os.getenv("TWITTER_PASSWORD")

        # Commented out the log in page since I am using my main browser session
        #  so there is no need to keep logging in. Adjust according to needs.

        # Open a new tab for the Twitter login

        # self.driver.execute_script("window.open('https://x.com/i/flow/login?mx=2', '_blank');")
        self.driver.execute_script("window.open('https://x.com/home', '_blank');")
        self.driver.switch_to.window(self.driver.window_handles[-1])
        # self.driver.get("https://x.com/i/flow/login")
        #
        # login_user = WebDriverWait(self.driver, 15).until(
        #     ec.element_to_be_clickable((By.XPATH,
        #                                 '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[4]/label/div/div[2]/div/input'))
        # )
        # login_user.send_keys(xusername)
        #
        # next_button = self.driver.find_element(By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/button[2]/div')
        #
        # # next_button = self.driver.find_element(By.CSS_SELECTOR, ".css-1jxf684.r-dnmrzs.r-1udh08x.r-1udbk01.r-3s2u2q.r-bcqeeo.r-1ttztb7.r-qvutc0.r-poiln3.r-a023e6.r-rjixqe")
        # next_button.click()
        #
        # # login_pass = WebDriverWait(self.driver, 15).until(
        # #     ec.element_to_be_clickable((By.CSS_SELECTOR,
        # #                                 ".r-30o5oe.r-1dz5y72.r-13qz1uu.r-1niwhzg.r-17gur6a.r-1yadl64.r-deolkf.r-homxoj.r-poiln3.r-7cikom.r-1ny4l3l.r-t60dpp.r-fdjqy7"))
        # # )
        # login_pass = WebDriverWait(self.driver, 15).until(
        #     ec.element_to_be_clickable((By.XPATH,
        #                                 '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input'))
        # )
        # login_pass.send_keys(xpassword)
        #
        # # login = WebDriverWait(self.driver, 15).until(
        # #     ec.element_to_be_clickable((By.CSS_SELECTOR,
        # #                                 ".css-146c3p1.r-bcqeeo.r-qvutc0.r-37j5jr.r-q4m81j.r-a023e6.r-rjixqe.r-b88u0q.r-1awozwy.r-6koalj.r-18u37iz.r-16y2uox.r-1777fci"))
        # # )
        # login = WebDriverWait(self.driver, 15).until(
        #     ec.element_to_be_clickable((By.XPATH,
        #                                 '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[1]/div/div/button/div'))
        # )
        # login.click()


        post_message = f"My promised internet speed was {PROMISED_DOWN}/{PROMISED_UP} but it is {self.down}/{self.up}."
        time.sleep(10)
        post_button = WebDriverWait(self.driver, 15).until(
            ec.element_to_be_clickable((By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div/div/div[1]/div/div/div/div/div/div[2]/div/div'))
        )
        # post_button = self.driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div/div/div[1]/div/div/div/div/div/div[2]/div/div')
        post_button.send_keys(post_message)

        send_button = WebDriverWait(self.driver, 15).until(
            ec.element_to_be_clickable((By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[2]/div[2]/div/div/div/button'))
        )
        send_button.click()



test = InternetSpeedTwitterBot()
try:
    test.get_internet_speed()
    if float(test.down) < PROMISED_DOWN or float(test.up) < PROMISED_UP:
        test.tweet_at_provider()

except Exception as e:
    print(f"An error occured: {e}")

finally:
    test.driver.quit()