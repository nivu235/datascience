import pandas as pd
df=pd.read_csv("realestate.csv")
print(df)
avg=df[['city','price']].groupby('city').mean()
print("average listing price of property")
print(avg)
pro=df[df['bedrooms']>4]
print("the number of property with more than four bedrooms")
print(pro)
area=df[df['sqft_living']==df['sqft_living'].max()]
print("property with large sqft")
print(area)

