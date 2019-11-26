import numpy as np
import pandas as pd

currency_rates = pd.read_csv('currency_rates.csv', index_col = 0)
currency_rates.columns = ['to-USD', 'to-MYR', 'to-AUD', 'to-NZD', 'to-INR']

#Welcome Users to the converter
print ("""
Hi There! Thank you for choosing us as your principle currency converter.
Please follow the instructions as follows.
""")

rows = {0: 'USD', 1: 'MYR', 2: 'AUD', 3: 'NZD', 4: 'INR'}
columns: {0: 'to-USD', 1: 'to-MYR', 2: 'to-AUD', 3: 'to-NZD', 4: 'to-INR'}

start = input("Please enter the currency you want to convert out of: ")
print (start)

while start not in rows.keys():
    print ("Please enter a valid integer between 0 and 4.")
    print (start)

end = input("Please enter the currency you would like to convert to.")
print (end)

while end not in rows.keys():
    print ("Please enter a valid integer between 0 and 4.")
    print (end)

loc_row = 0
loc_column = 0

loc_row = rows.pop(start)
loc_column = columns.pop(end)

conv_factor = currency_rates.iloc[[loc_row],[loc_column]]

start_val = input ("Please enter the amount of money you would like to convert: ")
print (start_val)
try:
   val = int(start_val)
   print("Yes input string is an Integer.")
   print("Input number value is: ", val)
except ValueError:
   print("That's not an int!")
   print("No.. input string is not an Integer. It's a string")

#convert start_val to a real number for conversion purposes
########

end_val = start_val * conv_factor
print (rows.pop(end) + end_val)

print ("Thank you for using the service. Have a good day")
 




