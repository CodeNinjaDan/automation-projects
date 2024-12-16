#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from data_manager import DataManager
from flight_search import FlightSearch


data_manager = DataManager()
sheety_data = data_manager.get_iata()
iatacode = [prices['iataCode'] for prices in sheety_data]
city_name = [prices['city'] for prices in sheety_data]

for code,city in zip(iatacode, city_name):
    pass

