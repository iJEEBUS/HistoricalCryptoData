import historicalData as hd

eth = ('ethereum')
btc = ('bitcoin')

print 'Ethereum'
print hd.getHistoricalData(eth)

print 'Bitcoin'
print hd.getHistoricalData(btc)