import requests
import os
from dotenv import load_dotenv

load_dotenv()

class FlightSearch:

    def __init__(self):
        self.amadeus_api_key = os.getenv("AMADEUS_API_KEY")
        self.amadeus_api_secret = os.getenv("AMADEUS_API_SECRET")
        self.access_token = self.new_access_token()




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
        print(f"Your token is {response.json()['access_token']}")
        print(f"Your token expires in {response.json()['expires_in']} seconds")
        return response.json()['access_token']


    def iata_search(self, city_name):
        """
        :return:
        str: The IATA code of the first matching city if found; "N/A" if no match is found due to an IndexError,
        or "Not Found" if no match is found due to a KeyError.

        The function sends a GET request to the IATA_ENDPOINT with a query that specifies the city
        name and other parameters to refine the search. It then attempts to extract the IATA code
        from the JSON response.
        - If the city is not found in the response data (i.e., the data array is empty, leading to
        an IndexError), it logs a message indicating that no airport code was found for the city and
        returns "N/A".
        - If the expected key is not found in the response (i.e., the 'iataCode' key is missing, leading
        to a KeyError), it logs a message indicating that no airport code was found for the city
        and returns "Not Found".
        """
        print(f"Using this token to get destination {self.access_token}")
        city_url = "https://test.api.amadeus.com/v1/reference-data/locations/cities"
        headers = {"Authorization": f"Bearer {self.access_token}"}
        city_params = {
            "keyword": city_name,
            "max": 2,
            "include": "AIRPORTS",
        }
        response = requests.get(url=city_url, params=city_params, headers=headers)

        print(f"Status code {response.status_code}. Airport IATA: {response.text}")
        try:
            code = response.json()["data"][0]['iataCode']
        except IndexError:
            print(f"IndexError: No airport code found for {city_name}.")
            return "N/A"
        except KeyError:
            print(f"KeyError: No airport code found for {city_name}.")
            return "Not Found"

        return code

    # # Request flight data
    # def get_flight_data(self):
    #     flights_url = "https://test.api.amadeus.com/v1/shopping/flight-destinations"
    #     headers = {"Authorization": f"Bearer {self.access_token}"}
    #
    #
    #     amadeus_params = {
    #         "origin":"PAR",
    #         "maxPrice": 300
    #     }
    #
    #     response = requests.get(url=flights_url, params=amadeus_params, headers=headers)
    #     data = response.json()
    #     pprint.pprint(data)
