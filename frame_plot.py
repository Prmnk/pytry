from pandas import DataFrame, Series
import pandas as pd
import matplotlib.pyplot as plt

filename='abc.txt'
dataset= pd.read_csv(filename)
frame = DataFrame(dataset)
print frame ['Open'][:10]
fig = plt.figure()
frame.plot()
plt.show()