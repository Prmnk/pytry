from pandas import DataFrame, Series
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import matplotlib.dates as mdates

filename='tsla.txt'
dataset= pd.read_csv(filename)
frame = DataFrame(dataset)
frame.columns=['date', 'closep', 'highp', 'lowp', 'openp', 'volume']
frame['diff']= (frame['highp']-frame['lowp'])/frame['lowp']
print frame[['date','diff']]

'''fig = plt.figure()
ax1 = plt.subplot(1,1,1)
#ax1.plot(frame['date'],frame['diff'])
ax1.plot(frame['date'],frame['highp'])
ax1.plot(frame['date'],frame['lowp'])

#ax1.xaxis.set_major_locator(mticker.MaxNLocator(10))
#ax1.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
plt.show()'''

name=frame.pivot_table('diff',rows=)