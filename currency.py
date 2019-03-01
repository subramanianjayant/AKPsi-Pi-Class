import pandas_datareader as pdr
import datetime

tags = ['DEXUSEU', 'DEXJPUS', 'DEXCAUS', 'DEXUSUK']

rates = pdr.DataReader(tags,'fred').tail(1)

print(rates)
