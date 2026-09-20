import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('HousePrices.csv', parse_dates=['date'], index_col='date')

df.sort_index(inplace=True)

print(df.head())

plt.plot(df['price'])
plt.show()

plt.hist(df['sqft_living'])
plt.show()

plt.xlabel('Price')
plt.ylabel('Sqft Living')
plt.title('Scatter Plot')
plt.scatter(x=df['price'], y=df['sqft_living'])
plt.show()

d = {'a': 10, 'b': 20, 'c': 13}

plt.bar(x=d.keys(), height=d.values())
plt.show()

plt.pie(x=d.values(), labels=d.keys())
plt.show()

plt.figure(figsize=(15, 10), dpi=100)
plt.plot(df['price'], label='Price')
plt.xlabel('Time')
plt.ylabel('Price')
plt.title('Line Plot of Prices')
plt.legend()
plt.show()
