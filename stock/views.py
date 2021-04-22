from django.shortcuts import render
import requests, os

def overview(request):
    response = requests.get(f"{os.getenv('API_URL')}/api/v4/company-outlook?symbol=AAPL&apikey={os.getenv('API_KEY')}")
    data = response.json()
    
    revenue = 0
    for income in data['financialsQuarter']['income'][0:4]:
        revenue += income['revenue'] 

    cashFlow = 0
    for cash in data['financialsQuarter']['cash'][0:4]:
        cashFlow += cash['operatingCashFlow'] 

    earning = 0
    for income in data['financialsQuarter']['income'][0:4]:
        earning += income['netIncome'] 


    res_historical_price = requests.get(f"{os.getenv('API_URL')}/api/v3/historical-price-full/AAPL?from=2021-03-20&to=2021-04-20&apikey={os.getenv('API_KEY')}")
    historical_price = res_historical_price.json()
    historicalP = historical_price['historical']

    labels = []
    historicalPrices = []
    volumes = []
    for item in historicalP:
        labels.append(item['label'])
        volumes.append(item['volume'])
        historicalPrices.append(item['close'])


    return render(request, 'stock/company/overview.html', {
        'updatedDate': data['rating'][0]['date'],
        'price': data['profile']['price'],
        'symbol': data['profile']['symbol'],
        'marketCap': data['profile']['mktCap'],
        'exchange': data['profile']['exchangeShortName'],
        'Beta': data['profile']['beta'],
        '52WeekH': data['metrics']['yearHigh'],
        '52WeekL': data['metrics']['yearLow'],
        'fairValuePrice': data['ratios'][0]['priceFairValueTTM'],
        'PE': data['ratios'][0]['peRatioTTM'],
        'PB': data['ratios'][0]['priceToBookRatioTTM'],
        'PS': data['ratios'][0]['priceToSalesRatioTTM'],
        'PEG': data['ratios'][0]['priceEarningsToGrowthRatioTTM'],
        'DividendYield': data['ratios'][0]['dividendYielTTM'],
        'GrossMargin': data['ratios'][0]['grossProfitMarginTTM'],
        'OperatingMargin': data['ratios'][0]['operatingProfitMarginTTM'],
        'ProfitMargin': data['ratios'][0]['netProfitMarginTTM'],
        'DebtEquity': data['ratios'][0]['debtEquityRatioTTM'],
        'Revenue': revenue,
        'cashFlow': cashFlow,
        'earning': earning,
        'labels': labels,
        'volumes': volumes,
        'historicalPrices': historicalPrices
        })


def earning(request):
    return render(request, 'stock/company/earning.html', {'earning': 'hello world!'})
