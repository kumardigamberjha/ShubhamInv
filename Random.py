# import requests

# url = "https://twelve-data1.p.rapidapi.com/stocks"

# querystring = {"country":"India","format":"json"}

# headers = {
# 	"X-RapidAPI-Key": "feadecd2b2mshbf33e9747918c7dp12c8a2jsn0f2a689d6525",
# 	"X-RapidAPI-Host": "twelve-data1.p.rapidapi.com"
# }

# response = requests.get(url, headers=headers, params=querystring)

# print(response.json())


# import requests

# tweleve = "https://twelve-data1.p.rapidapi.com/stocks"

# querystring = {"country":"India",'exchange':'BSE', "format":"json"}

# headers = {
# 	"X-RapidAPI-Key": "feadecd2b2mshbf33e9747918c7dp12c8a2jsn0f2a689d6525",
# 	"X-RapidAPI-Host": "twelve-data1.p.rapidapi.com"
# }

# response = requests.get(tweleve, headers=headers, params=querystring)

# # print(response.json())
# data = response.json()
# print("Data: ", data['data'][3166]['name'])
# print("Data: ", data['data'][3166]['exchange'])

# name = data['data'][3166]['name']
# symbol = data['data'][3166]['symbol']
# exchange = data['data'][3166]['exchange']

# print("Length: ", len(data['data']))


# try:
#     for i in range(len(data['data'])):
#         symbol = data['data'][i]['symbol']
#         exchange = data['data'][i]['exchange']

#         url = f'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={symbol}.{exchange}&apikey=2B1P6MEWMO1DQ5DL'
#         r = requests.get(url)
#         stockprice = r.json()
#         print(stockprice)
# except:
#     pass



# import requests

# api_key = "2B1P6MEWMO1DQ5DL"  # Replace with your actual API key

# symbols = ["AAPL", "GOOGL", "MSFT"]  # Replace with the stock symbols you're interested in
# base_url = "https://www.alphavantage.co/query"

# data_dict = {}  # Initialize an empty dictionary

# for symbol in symbols:
#     query_params = {
#         "function": "TIME_SERIES_INTRADAY",
#         "symbol": symbol,
#         "interval": "1min", 
#         "apikey": api_key,
#     }
#     print("Query : ",query_params)
# response = requests.get(base_url, params=query_params)
# data = response.json()

# # print("Data: ", data)
# if "Time Series (1min)" in data:
#     latest_timestamp = max(data["Time Series (1min)"].keys())
#     latest_price = data["Time Series (1min)"][latest_timestamp]["4. close"]
#     data_dict[symbol] = latest_price
#     print("Data_Dict : ", data_dict)

# import yfinance as yf

# exchange = "NSE"  # Replace with "BSE" or any other exchange you're interested in

# # stock_list = yf.Tickers(f"{exchange}.BO")  # For NSE, use ".BO" extension, for BSE use ".BO" extension
# stock_list = yf.download(f"{exchange}.BO", period="1d") 
# data_dict = {}  # Initialize an empty dictionary

# # for stock in stock_list.tickers:
# #     stock_info = stock.info
# #     symbol = stock_info['symbol']
# #     if "regularMarketPrice" in stock_info:
# #         latest_price = stock_info["regularMarketPrice"]
# #         data_dict[symbol] = latest_price
# for symbol in stock_list.columns.levels[1]:
#         latest_price = stock_list["Close", symbol][-1]  # Get the latest closing price
#         data_dict[symbol] = latest_price
# print("Data_Dict : ", data_dict)

# import requests

# # replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
# # url = 'https://www.alphavantage.co/query?function=MARKET_STATUS&apikey=2B1P6MEWMO1DQ5DL'

# url = "https://serpapi.com/search.json?engine=google_finance&q=NIFTY 50:NSE&extended=true&api_key=e0c4a2d8a57c8417b72d12782096716a95ec7ab49d377dd1f07960be0a8da9b6"
# r = requests.get(url)
# data = r.json()

# print(data)

import requests

# url = "https://apiconnect.angelbroking.com"

# querystring = {"q":"RELIANCE","region":"India"}

# headers = {
# 	"X-RapidAPI-Key": "72ySf0ZS ",
# 	"X-RapidAPI-Host": "apidojo-yahoo-finance-v1.p.rapidapi.com"
# }

# response = requests.get(url, headers=headers, params=querystring)

# print(response.json())




# FOR BSE
# https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol=BPCL.BO&apikey=ZT190HZDN99BS851



url = "https://apiconnect.angelbroking.com"

headers = {
    "Authorization": "Bearer 72ySf0ZS",  # Replace with your actual RapidAPI key
}

response = requests.get(url, headers=headers)

if response.status_code == 200:
    data = response.json()
    print(data)
else:
    print("Error:", response.status_code)
