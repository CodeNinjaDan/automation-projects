import requests
import os
from dotenv import load_dotenv
from pprint import pprint
load_dotenv()

class DataManager:

    def __init__(self):
        self.api_url = os.getenv("SHEETY_URL")
        self.destination_data = {}


    # Get all the data from the sheet
    def get_destination_data(self):
        response = requests.get(url=self.api_url)
        data = response.json()
        self.destination_data = data['prices']
        return self.destination_data



    def update_iata_code(self):
        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(url=f"{self.api_url}/{city['id']}", json=new_data)
            print(response.text)
