import pandas as pd
import string
df = pd.read_csv('review.csv')
stopwords = ['the', 'and', 'is', 'in', 'it', 'of', 'to', 'for', 'with', 'on', 'at']

for i in df['customer review']:
    

    words= i.split()
    print(words)
    if(words='the'):
        
    
