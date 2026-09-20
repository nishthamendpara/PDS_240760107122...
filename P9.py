import pandas as pd
df=pd.read_csv('HousePrices.csv')
df.head()
df.size
df.memory_usage(deep=True)
df.dtypes

df
df.dtypes

df['date'] = pd.to_datetime(df['date'])
df['street'] = df['street'].astype(str)
df['city'] = df['city'].astype(str)
df['statezip'] = df['statezip'].astype(str)
df['country'] = df['country'].astype(str)

df.set_index(['date'], inplace=True)

df.memory_usage(deep=True)

df.size

df.head()

df['bedrooms'] = df['bedrooms'].astype('int8')
df['price'] = df['price'].astype('int32')

df.size

df.memory_usage(deep=True)
