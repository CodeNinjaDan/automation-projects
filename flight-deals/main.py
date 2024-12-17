#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from data_manager import DataManager
from flight_search import FlightSearch


data_manager = DataManager()
sheety_data = data_manager.get_iata()


flight_search = FlightSearch()
flight_search.new_access_token()  # Initial token fetch
iata_codes = flight_search.city_search()  # Get IATA codes

# Update the IATA codes in the Google Sheet
if iata_codes:
    for row in sheety_data:
        city = row['city']
        if city in iata_codes:
            data_manager.update_iata_code(row['id'], iata_codes[city])
else:
    print("Error: IATA codes could not be retrieved.")


flight_search.start_scheduler()

