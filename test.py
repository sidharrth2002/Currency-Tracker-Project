import numpy as np
import pandas as pd

currency_rates = pd.read_csv('currency_rates.csv', index_col = 0)
currency_rates.columns = ['to-USD', 'to-MYR', 'to-AUD', 'to-NZD', 'to-INR']

print (currency_rates ['to-USD'])
