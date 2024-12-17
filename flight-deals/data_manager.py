import requests
import os
from dotenv import load_dotenv
from pprint import pprint
load_dotenv()

#This class is responsible for talking to the Google Sheet.
class DataManager:

    def __init__(self):
        self.api_url = os.getenv("SHEETY_URL")
        # self.flight_search = FlightSearch()
        # self.iata_codes = self.flight_search.city_search()


    def get_iata(self, api_url=None, headers=None, params=None):
        if api_url is None:
            api_url = self.api_url
        response = requests.get(url=api_url, headers=headers, params=params)
        response.raise_for_status()  # Raise an exception for bad status codes (4xx or 5xx)
        data = response.json()
        pprint(data)
        return data['prices']


    def update_iata_code(self, row_id, iata_code):

        update_endpoint = f"{self.api_url}/{row_id}"
        new_data = {
            "price": {
                "iataCode": iata_code
            }
        }
        response = requests.put(update_endpoint, json=new_data)
        return response.json()

