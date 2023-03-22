import pandas as pd

s = pd.Series([x for x in range(1,11)])

print(s)

""" Using the iloc method"""
print(s.iloc[0])
print(s.iloc[5])

"""Using the iat method """

print(s.iat[0])
print(s.iat[8])


""" Using slice method with both positive
    and negative indexs """
print(s[5:9])
print(s[-4:-1])


""" Using the .where notation """
print(s.where(s%2==0))
print(s.where(s%2==0, 'Odd Number'))
print(s.where(s%2==0, s**2))
""" Give you NaN value if it not an even number """
print(s.where(s%2==0))

""" Drops NaN values from the list if any """
s.where(s%2==0, inplace=True)
print(s.dropna())

""" Fils in the NaN """
print(s.fillna('Filled Value'))

