import pandas as pd
data={'customer_id':[101,102,101,102,101,103,104,105,106,107],
      'order_date':['5-3-23','2-3-23','6-3-23','1-3-23','8-3-23','6-3-23','7-3-23','8-3-23','9-3-23','10-3-23'],
    'product_name':['brush','paste','brush','shoe','pen','shoe','pencil','pen','eraser','ink'],
      'order_quantity':[4,2,2,3,2,3,7,1,4,1]
      
      }
df=pd.DataFrame(data)
print(df)
a=df[["product_name","order_quantity"]].groupby("product_name").sum()
a.sort_values(by='order_quantity',ascending=False,inplace=True)
print("the top 5 products that have been sold the most in the past month")
print(a.head(5))

