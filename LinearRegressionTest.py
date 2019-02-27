import numpy as np
import pandas as pd
import scipy
import statsmodels.api as sm
import matplotlib.pyplot as plt
import seaborn as sns
import sklearn


data = pd.read_csv('C:\Srini\\1.01. Simple linear regression.csv')
print(data)
print(data.describe())  # This gives the most useful statistic for each column in the data frame
y = data['GPA']
x1 = data['SAT']
plt.scatter(x1, y)
plt.xlabel('SAT', fontsize=20)
plt.ylabel('GPA', fontsize=20)
# plt.show()

x = sm.add_constant(x1)
results = sm.OLS(y, x).fit()  # OLS - Ordinary least square regression

results.summary()
print(results.summary())

plt.scatter(x1, y)
yhat = 0.0017*x1 + 0.275
fig = plt.plot(x1, yhat, lw=4, c='orange', label='regression line')
plt.xlabel('SAT', fontsize=20)
plt.ylabel('GPA', fontsize=20)
plt.show()


