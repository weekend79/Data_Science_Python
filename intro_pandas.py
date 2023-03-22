import pandas as pd


l = [x for x in range(10)]
s = pd.Series(l)

print(s)
print(s[5])


s1 = pd.Series(l, index=['a','b','c','d','e','f','g','h','i','j'])

print(s1)
print(s1['h'])

s2 = pd.Series(l, index=['a','b','c','d','e','f','g','h','h','j'])

print(s2['h'])


data = {'a':1,'b':2,'c':3,'d':4,'e':5}
s3 = pd.Series(data)

print(s3)

s4 = pd.Series(data, index=['a','b'])

print(s4)

""" This will throw a NaN in the value for m """
s5 = pd.Series(data, index=['a','b','c','m'])

print(s5)

