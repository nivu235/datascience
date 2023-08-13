import pandas as pd
import numpy as np
data=pd.read_csv('cars.csv')
print("csv data ")
print(data)
car_data=np.array(data)
print(car_data)
fuel=car_data[:,1]
print(fuel)
print("average fuel efficiency of car",int(np.mean(fuel)))
model1=car_data[:1,1]
print(model1)
model2=car_data[-4:-3,1]
print(model2)
avg=(model1)-(model2)
print("the percentage improvement in fuel efficiency between two car models",(avg)/model2*100,"%")





