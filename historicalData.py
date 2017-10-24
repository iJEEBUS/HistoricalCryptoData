'''
	Filename: historicalData.py
	Author: Ronald Rounsifer
	Date created: 10/24/2017
	Date last modified: 10/24/2017
	Python version 2.7.13
'''

from bs4 import BeautifulSoup
import urllib

# Base URL to get the historical data
_url = 'https://coinmarketcap.com/currencies/'

"""
Be able to input arguments to pick a coin, start/end date,
"""
def getHistoricalData(*coin):
	_url = 'https://coinmarketcap.com/currencies/'
	if coin:
		if len(coin) == 1:
			user_coin = coin[0]
			_url += user_coin + '/historical-data/?start=20130428&end=20171024'

	url = urllib.urlopen(_url)

	soup = BeautifulSoup(url ,'html.parser')

	table = soup.tbody
	data = table.find_all('td')
	allData = []

	for x in data:
		allData.append(x.get_text())

	enumerated_data = enumerate(allData, start=1)
	final_data = createList(enumerated_data)
	dictionary = createDictionary(final_data)
	return dictionary
	

"""
Creates a list of lists that contains each days information including:
Date
Open
High
Low
Close
Volume
Market Cap
"""
def createList(list):
	temp_holder = []
	temp = []
	historicalData = {
					"Date": "",
					"Open": "",
					"High": "",
					"Low": "",
					"Close": "",
					"Volume": "",
					"Market Cap": "",
					}
	for x in list:
		if x[0] % 7 == 0:
			temp.append(x[1])
			temp_holder.append(temp)
			temp = []
		else:
			temp.append(x[1])
	return temp_holder



"""
Creates a dictionary from a list containing the following:
Date
Open
High
Low
Close
Volume
Market Cap
The input is a list in a format that is produced from the createList function.
"""
def createDictionary(list):
	enum = enumerate(list, start=1)
	temp = []

	historicalData = {
					"Date": "",
					"Open": "",
					"High": "",
					"Low": "",
					"Close": "",
					"Volume": "",
					"Market Cap": "",
					}

		## TODO
		## ONLY ADDS DATA PER FOR EACH COLUMN OF EVERY 7 DAYS.
	for x in enum:
		if x[0] % 7 == 1:
			historicalData['Date'] = x[1][0]
		if x[0] % 7 == 2:
			historicalData['Open'] = x[1][1]
		if x[0] % 7 == 3:
			historicalData['High'] = x[1][2]
		if x[0] % 7 == 4:
			historicalData['Low'] = x[1][3]
		if x[0] % 7 == 5:
			historicalData['Close'] = x[1][4]
		if x[0] % 7 == 6:
			historicalData['Volume'] = x[1][5]
		if x[0] % 7 == 0:
			historicalData['Market Cap'] = x[1][6]
			temp.append(historicalData)
			historicalData = {
					"Date": "",
					"Open": "",
					"High": "",
					"Low": "",
					"Close": "",
					"Volume": "",
					"Market Cap": "",
					}
	return temp

"""
Returns all of the dates for the information in the dictionary
"""
def getDates(dictionary):
	temp = []
	for x in dictionary:
		temp.append(x['Date'])
	return temp
"""
Returns all of the open prices for the information in the dictionary
"""
def getOpenPrices(dictionary):
	temp = []
	for x in dictionary:
		temp.append(x['Open'])
	return temp

"""
Returns all of the high of the day prices for the information in the dictionary
"""
def getHighPrices(dictionary):
	temp = []
	for x in dictionary:
		temp.append(x['High'])
	return temp

"""
Returns all of the low of the day prices for the information in the dictionary
"""
def getLowPrices(dictionary):
	temp = []
	for x in dictionary:
		temp.append(x['Low'])
	return temp


"""
Returns all of the close prices for the information in the dictionary
"""
def getClosePrices(dictionary):
	temp = []
	for x in dictionary:
		temp.append(x['Close'])
	return temp

"""
Returns the volume for the information in the dictionary
"""
def getVolume(dictionary):
	temp = []
	for x in dictionary:
		temp.append(x['Volume'])
	return temp

"""
Returns the market cap for the information in the dictionary
"""
def getMarketCap(dictionary):
	temp = []
	for x in dictionary:
		temp.append(x['Market Cap'])
	return temp