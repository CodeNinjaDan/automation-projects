import time
import requests
import os
from dotenv import load_dotenv
import pprint
import schedule
from data_manager import DataManager

load_dotenv()
# This class is responsible for talking to the Flight Search API.

class FlightSearch:

    def __init__(self):
        self.amadeus_api_key = os.getenv("AMADEUS_API_KEY")
        self.amadeus_api_secret = os.getenv("AMADEUS_API_SECRET")
        self.access_token = None
        self.data_manager = DataManager()
        self.sheety_data = self.data_manager.get_iata()



    #Get a new access token since they expire after 30 mins
    def new_access_token(self):
        auth_url = "https://test.api.amadeus.com/v1/security/oauth2/token"
        auth_headers = {"Content-Type": "application/x-www-form-urlencoded"}
        auth_data = {
            "grant_type": "client_credentials",
            "client_id": self.amadeus_api_key,
            "client_secret": self.amadeus_api_secret
        }

        response = requests.post(auth_url, headers=auth_headers, data=auth_data)
        response.raise_for_status()
        self.access_token = response.json()["access_token"]
        print("New access token:", self.access_token)


    def start_scheduler(self):
        schedule.every(30).minutes.do(self.new_access_token)
        while True:
            schedule.run_pending()
            time.sleep(1)



    def city_search(self):
        iatacode = [prices['iataCode'] for prices in self.sheety_data]
        # city_name = [prices['city'] for prices in self.sheety_data]
        city_url = "https://test.api.amadeus.com/v1/reference-data/locations/cities"
        headers = {"Authorization": f"Bearer {self.access_token}"}
        city_params = {
            "keyword": [prices['city'] for prices in self.sheety_data],
        }
        response = requests.get(url=city_url, params=city_params, headers=headers)
        data = response.json()
        pprint.pprint(data)


    # Request flight data
    def get_flight_data(self):
        flights_url = "https://test.api.amadeus.com/v1/shopping/flight-destinations"
        headers = {"Authorization": f"Bearer {self.access_token}"}


        amadeus_params = {
            "origin":"PAR",
            "maxPrice": 300
        }

        response = requests.get(url=flights_url, params=amadeus_params, headers=headers)
        data = response.json()
        pprint.pprint(data)









if __name__ == "__main__":
    flight_search = FlightSearch()
    flight_search.new_access_token() # Initial token fetch
    flight_search.city_search()
    flight_search.start_scheduler()