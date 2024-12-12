import requests
import os
from dotenv import load_dotenv
from twilio.rest import Client

load_dotenv()

STOCK = "MSTR"
COMPANY_NAME = "MicroStrategy Incorporated"

stock_api_key = os.getenv("STOCK_API_KEY")
news_api_key = os.getenv("NEWS_API_KEY")
account_sid = os.getenv("ACCOUNT_SID")
auth_token = os.getenv("AUTH_TOKEN")
STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

stock_parameters = {
    "function":"TIME_SERIES_DAILY",
    "symbol":STOCK,
    "apikey":stock_api_key,
}

news_parameters = {
    "q":COMPANY_NAME,
    "sortBy":"popularity",
    "apiKey":news_api_key,
    "pageSize":5,
    "page":1,
}
stock_response = requests.get(url=STOCK_ENDPOINT, params=stock_parameters)
stock_response.raise_for_status()
stock_data = stock_response.json()

# #Get hold of the first day's close value
first_day_close = stock_data["Time Series (Daily)"][list(stock_data["Time Series (Daily)"].keys())[0]]["4. close"]
second_day_close = stock_data["Time Series (Daily)"][list(stock_data["Time Series (Daily)"].keys())[1]]["4. close"]


close_difference = (float(second_day_close) - float(first_day_close)) * -1
price_change = 5/100 * float(first_day_close)

if close_difference >= price_change or close_difference <= -price_change:
    # Fetch the first 3 articles for the COMPANY_NAME.
    news_response = requests.get(url=NEWS_ENDPOINT, params=news_parameters)
    news_response.raise_for_status()
    news_data = news_response.json()
    news_title = news_data["articles"][0:3]

    # Send a separate message with each article's title and description to your phone number.
    news_titles = [article['title'] for article in news_title]
    news_messages = [article['description'] for article in news_title]
    message_url = [article['url'] for article in news_title]

    client = Client(account_sid, auth_token)
    try:
        for title, message, url in zip(news_titles, news_messages, message_url):
            if price_change >= 5:
                formatted_message = f"{STOCK}: 🔺{price_change}% Headline: {title}\nBrief: {message}\nRead more: {url}"
            elif price_change <= -5:
                formatted_message = f"{STOCK}: 🔻{price_change}% Headline: {title}\nBrief: {message}\nRead more: {url}"

            message = client.messages.create(
                from_=os.getenv("WHATSAPP_SENDER"),
                body=formatted_message,
                to=os.getenv("WHATSAPP_RECEIVER"),
            )
            print(message.status)
    except Exception as e:
        print(f"An error occurred: {e}")
