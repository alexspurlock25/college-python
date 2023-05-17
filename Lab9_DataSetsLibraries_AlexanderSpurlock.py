# Alexander Spurlock
# 11/03/2022
# Lab 9: Data Sets

import pandas

df = pandas.read_csv('wic_ebt.csv', names=['countyname','effectivedate','foodcategory','food_subcategory','issuedqty','redeemedqty','redemption_rate'])

print(df.values)
print(df.info())
print(df.head())
print(df.tail())
print(df['countyname'])
print(df['countyname'].value_counts())
print(df[100:104])