import numpy as np
salesdata = []
for i in range(5):
    a= int(input("Enter the sales data:"))
    salesdata.append(a)
b=np.array(salesdata)
print(b)
av= np.mean(salesdata)
print("Average price of all products sold in the past month:", av)
