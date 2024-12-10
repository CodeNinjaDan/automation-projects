import requests
import os
from dotenv import load_dotenv
from twilio.rest import Client

load_dotenv()

account_sid = os.getenv("ACCOUNT_SID")
auth_token = os.getenv("AUTH_TOKEN")

OWM_Endpoint ="https://api.openweathermap.org/data/2.5/forecast"
lat = os.getenv("LAT")
lon = os.getenv("LON")
api_key = os.getenv("API_KEY")

parameters = {
    "lat":lat,
    "lon":lon,
    "appid":api_key,
    "cnt":4,
}

response = requests.get(OWM_Endpoint, params=parameters)
response.raise_for_status()
data = response.json()


will_rain = False
for day in data['list']:
    weather_id = (day['weather'][0]['id'])
    if weather_id < 700:
        will_rain = True
if will_rain:
    client = Client(account_sid, auth_token)

    try:
        message = client.messages.create(
            body="It's going to rain today. Bring an ☂️",
            from_=os.getenv("SENDER_NUMBER"),
            to=os.getenv("RECEIVER_NUMBER"),
        )
        print(message.status)
    except Exception as e:
        print(f"An error occurred: {e}")
