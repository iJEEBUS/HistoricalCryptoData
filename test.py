'''
	Filename: historicalData.py
	Author: Ronald Rounsifer
	Date created: 10/24/2017
	Date last modified: 10/24/2017
	Python version 2.7.13
'''

import historicalData as hd

eth_tuple = ('ethereum')
btc_tuple = ('bitcoin')

eth_data = hd.getHistoricalData(eth_tuple)
eth_open = hd.getOpenPrices(eth_data)
eth_close = hd.getClosePrices(eth_data)
eth_high = hd.getHighPrices(eth_data)
eth_low = hd.getLowPrices(eth_data)
eth_volume = hd.getVolume(eth_data)
eth_market_cap = hd.getMarketCap(eth_data)



"""
Sums the numbers together for the inputted prices
"""
def add(prices):
	total = 0
	for x in prices:
		total += float(x)
	return total

all_added = add(eth_close)
print len(eth_close)