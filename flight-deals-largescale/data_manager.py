import os
import requests
from dotenv import load_dotenv
from pprint import pprint

load_dotenv()


class DataManager:
    """
    This class is responsible for:
    1. Getting the destination data
    2. Updating the destination iata code
    3. Getting the user's email from the Google sheet (entered from a Google Form)

    """

    def __init__(self):
        self.prices_endpoint = os.environ["SHEETY_PRICE_URL"]
        self.users_endpoint = os.environ["SHEETY_USERS_URL"]
        self.destination_data = {}
        self.customer_data = {}

    def get_destination_data(self):
        # Use the Sheety API to GET all the data in that sheet and print it out.
        response = requests.get(url=self.prices_endpoint)
        data = response.json()
        # pprint(data)

        #Gets and stores the whole table
        self.destination_data = data["prices"]
        return self.destination_data

    # Make a PUT request and use the row id from sheet_data
    # to update the Google Sheet with the IATA codes.
    def update_destination_codes(self):
        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(
                url=f"{self.prices_endpoint}/{city['id']}",
                json=new_data
            )
            print(response.text)


    def get_customer_emails(self):
        response = requests.get(url=self.users_endpoint)
        data = response.json()
        # pprint(data)
        self.customer_data = data["users"]
        return self.customer_data