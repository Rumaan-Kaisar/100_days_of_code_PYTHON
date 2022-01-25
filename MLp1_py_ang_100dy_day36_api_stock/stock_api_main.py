STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

STOCK_KEY = "----------"
NEWS_KEY = "----------"

    ## STEP 1: Use https://www.alphavantage.co/documentation/#daily
# When stock price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
import requests
import json

# replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key

parMs = {
    "function" : "TIME_SERIES_DAILY",
    "symbol" : STOCK_NAME,
    "apikey" : STOCK_KEY
}

"""uRl = 'https://www.alphavantage.co/query'
r = requests.get(url= uRl, params= parMs )
data = r.json()"""

# Once data stored we access them 
with open(file = "data.json", mode= "r") as dt_file:
    data= json.load(dt_file)

# to access previous days data we need to use index, instead of hard coaded "2022-01-24"
# Hence list conversion needed. Use list comprehension
refined_data = data["Time Series (Daily)"]
data_list = [value for (key, value) in refined_data.items()]
yesterday = data_list[0]
day_before_yesterday = data_list[1]

yesterday_closing = data_list[0]["4. close"]
day_before_yesterday_closing = data_list[1]["4. close"]

print(f"yesterday = {data_list[0]}\n day_before_yesterday = {data_list[1]}")
print(yesterday_closing)
print(day_before_yesterday_closing)
# with open(file = "data.json", mode= "a+") as dt_file:
#     json.dump(data, dt_file, indent= 4)



abs_diff = abs(float(yesterday_closing) - float(day_before_yesterday_closing))

print(abs_diff)

diff_percent = (abs_diff/float(yesterday_closing))*100
print(diff_percent)

# If  percentage is greater than 1.2 then print("Get News")
if diff_percent > 1.2:
    print("Get News")

    news_param = {
        "qInTitle":COMPANY_NAME,
        "apiKey": NEWS_KEY
    }

    # news_respns = requests.get(url= NEWS_ENDPOINT, params= news_param)

    # with open(file = "news_data.json", mode= "a+") as dt_file:
    #     json.dump(news_respns.json(), dt_file, indent= 4)

    # arTicles = news_respns.json()["articles"]
    with open(file = "news_data.json", mode= "r") as dt_file:
        news_data= json.load(dt_file)
    arTicles = news_data["articles"]
    # print(arTicles)

    # GET first three articles, by slicing list. 4th index ie. 3 is needed, list-comprehension for print
    [print(f"Title : {artc['title']}\n\nDetails : {artc['description']}\n\n\n") for artc in arTicles[0 : 3]]

    # GET https://newsapi.org/v2/everything?q=keyword&apiKey=9e60e53105d2424faea4b1fb8151d89e

#TODO 1. - Get yesterday's closing stock price. Hint: You can perform list comprehensions on Python dictionaries. e.g. [new_value for (key, value) in dictionary.items()]

#TODO 2. - Get the day before yesterday's closing stock price

#TODO 3. - Find the positive difference between 1 and 2. e.g. 40 - 20 = -20, but the positive difference is 20. Hint: https://www.w3schools.com/python/ref_func_abs.asp

#TODO 4. - Work out the percentage difference in price between closing price yesterday and closing price the day before yesterday.

#TODO 5. - If TODO4 percentage is greater than 5 then print("Get News").

    ## STEP 2: https://newsapi.org/ 
    # Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 

#TODO 6. - Instead of printing ("Get News"), use the News API to get articles related to the COMPANY_NAME.

#TODO 7. - Use Python slice operator to create a list that contains the first 3 articles. Hint: https://stackoverflow.com/questions/509211/understanding-slice-notation


    ## STEP 3: Use twilio.com/docs/sms/quickstart/python
    #to send a separate message with each article's title and description to your phone number. 

#TODO 8. - Create a new list of the first 3 article's headline and description using list comprehension.

#TODO 9. - Send each article as a separate message via Twilio. 



#Optional TODO: Format the message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

# python stock_api_main.py