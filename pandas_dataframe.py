import pandas
import pandas as pd


df = pd.DataFrame()
type(df)
pandas.core.frame.DataFrame
df = pd.read_csv(r'C:\Users\EntroBet\Desktop\PlayerSearch.csv')

print(df)
print(df.head())
print(df.tail())


print(df.head(2))
print(df.tail(2))

print(df.iloc(0))
print(df.tail(3))


print(df.values)


df2 = pd.read_csv(r'C:\Users\EntroBet\Desktop\PlayerSearch.csv', chunksize=20)
for chunk in df2:
    print(chunk)

df3 = pd.read_csv(r'C:\Users\EntroBet\Desktop\PlayerSearch.csv')
df3 = df3[df3['ID']<677461]
print(df3)
