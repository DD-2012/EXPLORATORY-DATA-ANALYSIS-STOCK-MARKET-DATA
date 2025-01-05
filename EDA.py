import yfinance as yf 
import numpy as np  
import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns         
from scipy import stats  
from datetime import datetime 
from google.colab import files  
#download historical data 
ticker='GOOG' 
data1=yf.download(ticker,start='2015-01-01',end='2024-11-30') 
#understand the data 
data1.shape  
data1.info ()  
#Visualize few rows 
data1.head() 
# index to column conversion 
data2=data1.reset_index()
data2['Date']=pd.to_datetime(data2['Date']) 
#data2['Date'] = data2['Date'].dt.strftime('%Y-%m-%d')  
data2.head() 

#visualization 
data2['Date'] = pd.to_datetime(data2['Date']) 
plt.figure(figsize=(12, 6))  
plt.plot(data2['Date'], data2['Close'], marker='o', linestyle='-', color='b') 
plt.xlabel('Date') 
plt.ylabel('Closing Price') 
plt.title(' Closing Prices Over Time') 
plt.xticks(rotation=45)  # adjust ticks on x-axis 
plt.grid() 
plt.tight_layout()  # automatically adjust plots- avoid overlapping 
plt.show() 

#data cleaning 
# Checks for missing values and prints total counts of missing values for each column 
data2.isnull().sum() 
#print (data2. isnull().sum()) 
#remove rows with (not a number(nan), missing values) 
data2= data2.dropna() 
# Checks for duplicate rows and prints total number of duplicates 
print(data2.duplicated().sum()) 
# remove any duplicate rows, keep=remove all duplicates and inplace-modifies the 
original data frame 
data2.drop_duplicates (keep=False, inplace=True) 

#descriptive statistics 
print("summary statistics:") 
price_stats = data2.select_dtypes(include=['float64', 'int64']).describe() 
price_stats 

#Univariate analysis- distribution of closing price 
plt.figure(figsize=(12, 6)) 
sns.histplot(data2['Close'],kde=True, bins=50) 
approximation of data's distribution 
plt.title('Univariate analysis : Distribution of Closing  Price') 
plt.xlabel('Closing Price') 
plt.ylabel('Frequency') 
plt.show() 

# Bivariate analysis
fig, ax = plt.subplots(figsize=(10,6)) 
ax.scatter(data2['Volume'], data1['Close'],color='green') 
ax.set_xlabel('Volume') 
ax.set_ylabel('Close') 
plt.show() 

#Multivariate analysis 
corr = data2[['Open', 'High', 'Low', 'Close']].corr() 
plt.figure(figsize=(8,8)) 
sns.heatmap(corr, annot=True, cmap='coolwarm') 
plt.title('Correlation Heatmap') 
plt.show()
