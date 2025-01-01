import time
from data_manager import DataManager
from flight_search import FlightSearch
from flight_data import FlightData
from notification_manager import NotificationManager
# ==================== Set up the Flight Search ====================

data_manager = DataManager()
sheet_data = data_manager.get_destination_data()
flight_search = FlightSearch()
notification_manager = NotificationManager()

# ==================== Update the Airport Codes in Google Sheet ====================


for row in sheet_data:
    if row["iataCode"] == "":
        row["iataCode"] = flight_search.iata_search(row["city"])
        # slowing down requests to avoid rate limit
        time.sleep(2)
print(f"sheet_data:\n {sheet_data}")

data_manager.destination_data = sheet_data
data_manager.update_iata_code()


# ================================= Get the cheap flight data =================================

# Store the price data for each flight
flight_data_list = []
for row in sheet_data:
    flight_data = FlightData(
        price=row["lowestPrice"],
        departure_airport_code=row["iataCode"],
        origin_airport="SYD",
        destination_airport=row["iataCode"],
        out_date="2025-01-10",
        return_date="2025-06-01"
    )
    flight_data_list.append(flight_data)


# Print the stored flight data
for flight in flight_data_list:
    print(f"Price: {flight.price}, Departure Airport Code: {flight.departure_airport_code}")

# Define cheapest_flight and destination
cheapest_flight = min(flight_data_list, key=lambda x: x.price)
destination = next((row for row in sheet_data if row["iataCode"] == cheapest_flight.departure_airport_code), None)

# Send notification
if cheapest_flight.price != "N/A" and cheapest_flight.price < destination["lowestPrice"]:
    print(f"Lower price flight found to {destination['city']}!")


    notification_manager.send_whatsapp(
        message_body=f"Low price alert! Only £{cheapest_flight.price} to fly "
                     f"from {cheapest_flight.origin_airport} to {cheapest_flight.destination_airport}, "
                     f"on {cheapest_flight.out_date} until {cheapest_flight.return_date}."
    )
