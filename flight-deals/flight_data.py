import requests
import os
from dotenv import load_dotenv
from datetime import datetime, timedelta
from pprint import pprint

load_dotenv()

#Structure the flight data.
class FlightData:

    def __init__(self, price, departure_airport_code, origin_airport, destination_airport, out_date, return_date):
        self.price = price
        self.departure_airport_code = departure_airport_code
        self.origin_airport = origin_airport
        self.destination_airport = destination_airport
        self.out_date = out_date
        self.return_date = return_date



    def find_cheapest_flight(self, maxprice, access_token):
        flight_url = "https://test.api.amadeus.com/v2/shopping/flight-offers"
        params = {
            "originLocationCode": "SYD",
            "destinationLocationCode": self.departure_airport_code,
            "departureDate": self.out_date,
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


