# Python
Requirement:  Pandas

Assumptions:  day, week, month and year are not calendar periods. Instead, they are last 1, 7, 30 and 365 days respectively.

Used spot prices, instead of historic prices. Because, could not find API interface for historical prices for custom date. and typo error in API link 

Usage:

Point 1
python3  coinbasePrice.py '2018-11-01'   # Custom Date

{'2018-11-01': 6310.17}



python3  coinbasePrice.py -p day   # Last day


{'2018-11-10': 6355.71}



python3  coinbasePrice.py -p week  # Last week


{'2018-11-10': 6355.71, '2018-11-09': 6366.55, '2018-11-08': 6451.04, '2018-11-07': 6506.34, '2018-11-06': 6413.17, '2018-11-05': 6405.13, '2018-11-04': 6365.53}



python3  coinbasePrice.py -p month  # Last month (last 30 days)

python3 coinbasePrice.py -p week  # Last year (last 365 days)








python3 coinbasePrice.py -b '2018-11-01' -e '2018-11-10' # Custom days


{'2018-11-01': 6310.17, '2018-10-31': 6275.73, '2018-10-30': 6264.21, '2018-10-29': 6330.31, '2018-10-28': 6403.84, '2018-10-27': 6407.16, '2018-10-26': 6399.89, '2018-10-25': 6400.52, '2018-10-24': 6423.83}



point 2



python3  coinbasePrice.py -b '2018-11-01' -e '2018-11-10' -s 4   # Moving Average of 4 days rolling window


{'Moving Average': {'2018-11-01': nan, '2018-10-31': nan, '2018-10-30': nan, '2018-10-29': 6295.1050000000005, '2018-10-28': 6318.5225000000009, '2018-10-27': 6351.380000000001, '2018-10-26': 6385.3000000000011, '2018-10-25': 6402.8525000000009, '2018-10-24': 6407.8500000000013}}

