import requests
import os
from dotenv import load_dotenv
import pprint

load_dotenv()

STOCK = "MSTR"
COMPANY_NAME = "MicroStrategy Incorporated"

stock_api_key = os.getenv("STOCK_API_KEY")
news_api_key = os.getenv("NEWS_API_KEY")
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
# stock_response = requests.get(url=STOCK_ENDPOINT, params=stock_parameters)
# stock_response.raise_for_status()
# stock_data = stock_response.json()
#
# #Get hold of the first day's close value
# first_day_close = stock_data["Time Series (Daily)"][list(stock_data["Time Series (Daily)"].keys())[0]]["4. close"]
# second_day_close = stock_data["Time Series (Daily)"][list(stock_data["Time Series (Daily)"].keys())[1]]["4. close"]

## STEP 1: Use https://newsapi.org/docs/endpoints/everything
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
#HINT 1: Get the closing price for yesterday and the day before yesterday. Find the positive difference between the two prices. e.g. 40 - 20 = -20, but the positive difference is 20.
#HINT 2: Work out the value of 5% of yesterday's closing stock price.
# close_difference = (float(second_day_close) - float(first_day_close)) * -1
# price_change = 5/100 * float(first_day_close)

# if close_difference >= price_change or close_difference <= -price_change:
#     print("Get News")

## STEP 2: Use https://newsapi.org/docs/endpoints/everything
# Instead of printing ("Get News"), actually fetch the first 3 articles for the COMPANY_NAME. 
#HINT 1: Think about using the Python Slice Operator
news_response = requests.get(url=NEWS_ENDPOINT, params=news_parameters)
news_response.raise_for_status()
news_data = news_response.json()
pprint.pprint(news_data)
news_title = news_data["articles"][0:3]
pprint.pprint(news_title)
## STEP 3: Use twilio.com/docs/sms/quickstart/python
# Send a separate message with each article's title and description to your phone number. 
#HINT 1: Consider using a List Comprehension.



#Optional: Format the SMS message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

