import pandas as pd
data={'post':[1,2,3,4,5,6,7],

    'likes':[200,300,200,400,220,300,220]
      
      }
df=pd.DataFrame(data)
print(df)
a=df['likes'].value_counts()
print("frequncy distribution of likes for post" )
print(a)
