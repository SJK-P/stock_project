from django.shortcuts import render
import requests, os

def overview(request):
    response = requests.get(f"{os.getenv('API_URL')}/quote/AAPL?apikey={os.getenv('API_KEY')}")
    quote_data = response.json()[0]
    return render(request, 'stock/overview/quote.html', {
        'price': quote_data['price'],
        'dayL': quote_data['dayLow'],
        'dayH': quote_data['dayHigh'],
        'yearH': quote_data['yearHigh'],
        'yearL': quote_data['yearLow'],
        'marketCap': quote_data['marketCap'],
        'earnAnnounce': quote_data['earningsAnnouncement'],
        'exchange': quote_data['exchange'],
        'prePrice': quote_data['previousClose']

        })


def earning(request):
    return render(request, 'stock/overview/earning.html', {'earning': 'hello world!'})
