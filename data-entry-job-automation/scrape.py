from bs4 import BeautifulSoup
import requests


class GetHouseData:
    """
    Constructor for scraping the zillow website and fetching the price, location and url to the listing
    for a house.

    Parameters:
        - response: fetches the webpage
        - zillow_web_page: proper formatting for BeautifulSoup
        - soup: for scraping the webpage
    """

    def __init__(self):
        try:
            response = requests.get("https://appbrewery.github.io/Zillow-Clone/")
            response.raise_for_status()
            zillow_web_page = response.text
            self.soup = BeautifulSoup(zillow_web_page, 'html.parser')

        except requests.exceptions.RequestException as e:
            print(f"Error fetching the URL: {e}")
            self.soup = None



    def scrape(self):

