
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.colors import LogNorm
from sklearn import mixture
import numpy as np
from scipy.stats import norm


data = pd.read_csv('lifeInsurance.txt', header = None, sep= '\s+')
data.columns = ['GENDER', 'AGE', 'Marital Status', 'Nmr of children', 'Life Style', 'Chronic Diseases', 'Salary (monthly)', 'Decision']  


######################################################################################
dataStr = data
dataStr['GENDER'] = dataStr['GENDER'].replace({0.0: 'Female', 1.0: 'Male'})
# print(data.head())
######################################################################################


colors = ['red' if dec == 0 else 'green' for dec in data['Decision']]

plt.figure(figsize=(10, 6))
# plt.subplot(1, 2, 1)
plt.scatter(data['Salary (monthly)'],
            data['Decision'],
            color=colors, 
            alpha=0.6, 
            label='Client Data')
plt.xlabel('Salary (€/month)')
plt.ylabel('Decision')
plt.title('Client Data: Salary vs Decision')

plt.yticks(ticks=[0, 1], labels=['No', 'Yes'])
plt.text(2000, 0.5, 'Aparentemente, o salário não quer dizer nada lol', dict(size=10))

plt.show()


