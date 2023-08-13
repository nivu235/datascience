import numpy as np
a=[]
for i in range(0,4+1):
    s= int(input("sales of the year:"))
    a.append(s)
salesdata=np.array(a)
print(salesdata)
total= np.sum(salesdata)
per= ((salesdata[4] - salesdata[0]) / salesdata[0]) * 100
print("Total sales for the year:", total)
print("Percentage increase in sales from Q1 to Q4:", per, "%")
