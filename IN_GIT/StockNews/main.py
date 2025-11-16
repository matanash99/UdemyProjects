import requests
import datetime as dt
from data import stock_data, news_data #helper to avoid calling api for tests
from twilio.rest import Client


# #
# ## STEP 1: Use https://www.alphavantage.co
# # When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
#
STOCK = "AAPL"
COMPANY_NAME = "Apple Inc"
STOCK_API_KEY = "C4N8Z87VWZ469TXZ"
CLOSE_INDEX = "4. close"
#
stock_parameters = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": STOCK_API_KEY
}

# Correct URL
stock_url = "https://www.alphavantage.co/query"

stock_request = requests.get(url=stock_url, params=stock_parameters)
stock_json = stock_request.json()


# stock_json = stock_data     #helper to avoid calling api for tests

last_days = list(stock_json["Time Series (Daily)"].keys())

# for i in range(10):
#     print(f"{i} - {float(stock_json["Time Series (Daily)"][last_days[i]][CLOSE_INDEX])}") # helper to know where is the highest jump for tests
first_date = last_days[0]
second_date = last_days[1]

recent_day_stock = float(stock_json["Time Series (Daily)"][first_date][CLOSE_INDEX])
second_day_stock = float(stock_json["Time Series (Daily)"][second_date][CLOSE_INDEX])

difference = recent_day_stock - second_day_stock
print(f"First - {recent_day_stock}")
print(f"Second - {second_day_stock}")


percentage_change = difference/recent_day_stock * 100
print(percentage_change)
if percentage_change >= 5:
    print("Get news")








## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.
NEWS_API_KEY = "c39f26204a9743d9a5b9cd54f8529a9b"
news_url = "https://newsapi.org/v2/everything"

parameters = {
    "q": "Apple Inc",
    "sortBy": "publishedAt",
    "apiKey": NEWS_API_KEY,
    "language": "en"
}

news_request = requests.get(url= news_url, params= parameters)
news_json = news_request.json()
# print(news_request)
# print(news_json)

# news_json = news_data #helper to avoid calling api for tests

last_articles = list(news_json["articles"])
article_one = last_articles[0]
article_two = last_articles[1]
article_three = last_articles[2]

my_articles = [article_one, article_two, article_three]
formatted_articles = [f"Headline: {article['title']}. \nBrief: {article['description']}" for article in my_articles]
final = ""
if percentage_change > 0:
    final = f"{STOCK}: 🔺{percentage_change:.3f}\n"
else:
    final += f"{STOCK}: 🔻{(percentage_change * -1):.3f}\n"
i = 1
for article in formatted_articles:
    final+= f"Article {i}:\n{article}\n"
    i+=1

# print(final)   #final text that is sent






# ## STEP 3: Use https://www.twilio.com
# # Send a seperate message with the percentage change and each article's title and description to your phone number.
account_sid = 'AC83e859e340a210486b25ce6245083f13'
auth_token = '52fc5a23b32f814d68f3d59719b0bb8c'
client = Client(account_sid, auth_token)

message = client.messages.create(
  from_='whatsapp:+14155238886',
  # content_sid='HXb5b62575e6e4ff6129ad7c8efe1f983e',
  body= final,
  # content_variables='{"1":"24/6","2":"4:54PM"}',
  to='whatsapp:+972528514460'
)

print(message.sid)



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

