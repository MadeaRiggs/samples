from cgitb import html
from matplotlib.pyplot import table
import requests as req
from bs4 import BeautifulSoup
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#request data from website
html=req.get("https://www.worldometers.info/coronavirus")
print(html.content) #check downloaded content
html_parsed=BeautifulSoup(html.content) #parse html with BeautifulSoup
table=html_parsed.find('table', attrs={'id': 'main_table_countries_today'}) #search for the required table
print(table) #check results
rows=table.find_all("tr") #get all the rows
print(rows[0]) #check result
print(rows[0].text.strip())
print(rows[9].text.strip().split("\n")) #tokenization

#store rows nto list
data=[]
for x in rows:
    data.append(x.text.strip().split("\n")[1:5])
df=pd.DataFrame(data) #convert list into DataFrame
print(df.head()) #check DataFrame
#set the first row as the header, and remove the second row
df=pd.DataFrame(data[9:], columns=data[0]) 
print(df.head())
df.to_csv('covid19.csv') #save as CSV file

df_plot=df[['Country,Other', 'TotalCases']] #get the required columns
df_plot=df_plot[:10] #get the first 10 rows
print(df_plot.head())
#remove commas in digits, and convert string to int
df_plot['TotalCases']=df_plot['TotalCases'].apply(lambda x: x.replace(',', '')).astype(int)
print(df_plot.head())
#plot
df_plot.plot(kind='bar', x='Country,Other',y='TotalCases')
