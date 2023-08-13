import pandas as pd
data={'customer_id':[101,102,101,102,101,103,104],'order_date':['5-3-23','2-3-23','6-3-23','1-3-23','8-3-23','6-3-23','7-3-23'],
    'product_name':['brush','paste','brush','shoe','pen','shoe','pencil'],
      'order_quantity':[4,2,2,3,2,1,7]
      
      }
df=pd.DataFrame(data)
print(df)
a=df['customer_id'].value_counts()
print("total number of purchase of each customer")
print(a)
avg=df[["product_name","order_quantity"]].groupby("product_name").mean()
print(avg)
latestdate=df["order_date"].max()
oldestdate=df["order_date"].min()
print("Earliest order date is",latestdate)
print("oldest order date is",oldestdate)
