from datetime import date, datetime, timedelta
import requests, json, getopt, sys
import pandas as pd

def getDatesByPeriod(period):
	numDays = {'day':1, 'week':7, 'month':30, 'year':365}[period]
	beginDate = date.today() - timedelta(1)
	dates = [beginDate - timedelta(i) for i in range(numDays)]
	return dates

def getDatesByCustomiDates(beginDate, endDate):
	beginDate = datetime.strptime(beginDate, '%Y-%m-%d')
	endDate = datetime.strptime(endDate, '%Y-%m-%d')
	numDays = ((endDate-beginDate).days)    
	dates = [beginDate - timedelta(i) for i in range(numDays)]
	return dates


def getPrice(tgtDate):
    url='https://www.coinbase.com/api/v2/prices/BTC-USD/spot?date='+tgtDate
    req=requests.get(url)
    return float(req.json()['data']['amount'])


def main(argv):
    sma = False
    beginDate = ''
    endDate = ''
    period=''
    
    try:
        opts, args = getopt.getopt(argv,"hs:p:b:e:")
    except:
        print ('coinbasePrice.py -p <period> [-s] [date]')
        sys.exit(2)
    
    for opt, arg in opts:
        if opt == '-h':
            print ('a.py -p <period> [-s] [sma] date')
            sys.exit()
        elif opt == '-p':
            period = arg
        elif opt == '-s':
            try:
                sma = int(arg)
            except ValueError:
                print("Invalid rolling days")
                sys.exit(2)
        elif opt == '-b':
            try:
                beginDate = datetime.strptime(arg, '%Y-%m-%d')
            except ValueError:
                print("Invalid Date")
                sys.exit(2)
        elif opt == '-e':
            try:
                endDate = datetime.strptime(arg, '%Y-%m-%d')
            except ValueError:
                print("Invalid Date")
                sys.exit(2)
            
            
    if len(args) == 1:
        try:
            tgtDate = args[0]
            fPrice = getPrice(tgtDate)
            dPrice = {}
            dPrice[tgtDate] = fPrice
            print(dPrice)
            sys.exit()
        except ValueError:
            print("Invalid Date")
            sys.exit(2)
    
    if period in ['day', 'week', 'month', 'year']:
        dates = getDatesByPeriod(period)
        dPrices = {}
        for date in dates:
            tgtDate = datetime.strftime(date, '%Y-%m-%d')
            fPrice = getPrice(tgtDate)
            dPrices[tgtDate] = fPrice
        print(dPrices)
    
    if beginDate and endDate:
        beginDate = datetime.strftime(beginDate, '%Y-%m-%d')
        endDate = datetime.strftime(endDate, '%Y-%m-%d')
        dates = getDatesByCustomiDates(beginDate, endDate)
        dPrices = {}
        for date in dates:
            tgtDate = datetime.strftime(date, '%Y-%m-%d')
            fPrice = getPrice(tgtDate)
            dPrices[tgtDate] = fPrice
        if sma:
            df = pd.DataFrame(list(dPrices.items()), columns=['Date','Price'])
            smadf = df.rolling(window=sma).mean()
            smadf.columns = ['Date', 'Moving Average']
            smadf = smadf.set_index(['Date'])
            dSMA = smadf.to_dict()
            print(dSMA)
        else:
            print(dPrices)


if __name__ == "__main__":
   main(sys.argv[1:])
   