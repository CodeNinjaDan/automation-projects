import requests
import os
from dotenv import load_dotenv
from datetime import datetime

load_dotenv()

WEIGHT = 65
HEIGHT = 189
AGE = 19

today = datetime.now()
sheety_url = os.getenv("SHEETY_URL")
nutritionix_url = "https://trackapi.nutritionix.com/v2/natural/exercise"
bearer_token = os.getenv("SHEETY_BEARER_TOKEN")
sheety_headers = {"Authorization": f"Bearer {bearer_token}"}

nutritionix_headers = {
    "x-app-id": os.getenv("NUTRITIONIX_APP_ID"),
    "x-app-key": os.getenv("NUTRITIONIX_API_KEY"),
}
query_text = input("What workouts did you do?: ")
nutritionix_params = {
    "query": query_text,
    "weight_kg": WEIGHT,
    "height_cm": HEIGHT,
    "age": AGE,
}
response = requests.post(url=nutritionix_url, json=nutritionix_params, headers=nutritionix_headers)
result = response.json()

exercise = result["exercises"][0]["name"]
duration = result["exercises"][0]["duration_min"]
calories = result["exercises"][0]["nf_calories"]

sheety_params = {
    "workout": {
        "date": today.strftime("%d/%m/%Y"),
        "time": today.strftime("%X"),
        "exercise": exercise,
        "duration": duration,
        "calories": calories,
    }
}
update = requests.post(url=sheety_url, json=sheety_params, headers=sheety_headers)
