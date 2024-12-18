import requests
import os
from dotenv import load_dotenv
from datetime import datetime, timedelta
from pprint import pprint

load_dotenv()

#Structure the flight data.
class FlightData:

    def __init__(self, price, departure_airport_code):
        self.price = price
        self.departure_airport_code = departure_airport_code
        self.departure_date = (datetime.now() + timedelta(days = 1)).strftime('%Y-%m-%d')
        self.return_date = (datetime.now() + timedelta(days = 180)).strftime('%Y-%m-%d')



    def find_cheapest_flight(self, maxprice, access_token):
        flight_url = "https://test.api.amadeus.com/v2/shopping/flight-offers"
        params = {
            "originLocationCode": "SYD",
            "destinationLocationCode": self.departure_airport_code,
            "departureDate": self.departure_date,
            "returnDate": self.return_date,
            "adults": 1,
            "currencyCode": "EUR",
            "maxPrice" : maxprice,
            "max": 9
        }

        headers = {"Authorization": f"Bearer {access_token}"}

        response = requests.get(url=flight_url, headers=headers, params=params)
        response.raise_for_status()
        data = response.json()
        pprint(data)


