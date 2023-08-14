from django.shortcuts import render
import requests

def MarketsIndex(request):
    # tweleve = "https://twelve-data1.p.rapidapi.com/stocks"

    # querystring = {"country":"India",'exchange':'BSE', "format":"json"}

    # headers = {
    #     "X-RapidAPI-Key": "feadecd2b2mshbf33e9747918c7dp12c8a2jsn0f2a689d6525",
    #     "X-RapidAPI-Host": "twelve-data1.p.rapidapi.com"
    # }

    # response = requests.get(tweleve, headers=headers, params=querystring)

    # data = response.json()
    # length = 30

    # data_dict = {}  # Initialize an empty dictionary

    # for i in range(10, length):
    #     name = data['data'][i]['name']
    #     exchange = data['data'][i]['exchange']
    #     data_dict[name] = exchange

    # print("Arr : ", data_dict)
    # context = {'data': data, "Arr": data_dict}

    url = "https://latest-stock-price.p.rapidapi.com/price"

    querystring = {"Indices":"NIFTY 50"}
    # querystring1 = {"Indices":"NIFTY MIDCAP 100"}

    headers = {
        "X-RapidAPI-Key": "3751f4ece6msh3fe30b09007df0cp135a36jsn187187f1e616",
        "X-RapidAPI-Host": "latest-stock-price.p.rapidapi.com"
    }

    # combined_querystring = {**querystring, **querystring1}
    response = requests.get(url, headers=headers, params=querystring)

    # response = requests.get(url, headers=headers, params=querystring)

    data = response.json()
    # print("data: ", data)
    data_dict = {}  # Initialize an empty dictionary

    for i in range(10):
        name = data[i]['symbol']
        exchange = data[i]['lastPrice']
        data_dict[name] = exchange
    # print(response.json())
    print(data_dict)
    context = {'data': data, 'Arr': data_dict}
    return render(request, 'Markets/market_index.html', context)


def DetailStockInfo(request):
    if request.method == "GET":
        name = request.GET.get('name')
        exchange = request.GET.get('exchange')

    url = f'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=NSE:{name}.NSE&apikey=2B1P6MEWMO1DQ5DL'
    r = requests.get(url)
    print("R: ", r)
    stockprice = r.json()
    print("Name: ", name, stockprice)
    return render(request, 'Markets/detailinfo.html')  # Render an empty page for non-GET requests
