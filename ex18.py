import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats
data={'Age':[23,23,27,27,39,41,47,49,50,52,54,54,56,57,58,58,60,61],
      'fat':[9.5,26.5,7.8,17.8,31.4,25.9,27.4,27.2,31.2,34.6,
             42.5,28.8,33.4,30.2,34.1,32.9,41.2,35.7]
    }
df=pd.DataFrame(data)
print(df)
print("mean of age",df['Age'].mean())
print("median of age",df['Age'].median())
print("standard deviation of Age",df['Age'].std())
print("mean of fat",df['fat'].mean())
print("median of fat",df['fat'].median())
print("standard deviation of fat",df['fat'].std())
df['Age'].plot(kind='box', title='AGE')
plt.show()
df['fat'].plot(kind='box', title='weight')
plt.show()

stats.probplot(df['Age'], plot=plt)

plt.title("Q-Q Plot")
plt.show()

stats.probplot(df['fat'], plot=plt)

plt.title("Q-Q Plot")
plt.show()
