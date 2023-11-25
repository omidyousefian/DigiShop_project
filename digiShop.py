
import numpy as np 
import pandas as pd


"""
Created on Wed Feb 12 23:58:40 2020

@author: BigVaio
"""
# HomeWork 5 - digi2.csv


df=pd.read_csv('D:/DataScience/Data Science Course tihe/data sets/digi2.csv' , encoding='UTF-8')

# 1-Get the columns of the data frame df.  
df.columns

# 2-Count the number of missing values in the columns of this dataset.  Hint: use df.isna() 
sum(df.isna())
np.sum(df.isna())

# 3-Remove the column ‘Amount_Gross_Order’ since it is not well defined.  Hint: use df.drop()  
df=df.drop(columns='Amount_Gross_Order')
df.columns

# 4) Drop the duplicates in the dataset. Hint: df.drop_duplicates(inplace=True)
df.drop_duplicates(inplace=True)

# 5) Change the structure of the variable 'DateTime_CartFinalize' to timestamp. You can use pd.Timestamp function.
pip install persiantools
from persiantools.jdatetime import JalaliDate
v=JalaliDate(pd.Timestamp('1/9/2020'))
v.today
v.day
v.month
v.year
import datetime , pytz

df['DateTime']=df['DateTime_CartFinalize'].agg(pd.Timestamp)
df['DateTime']
   # Out[34]: 
#0        2015-10-15 08:50:00
#1        2018-02-11 00:29:00
#2        2016-06-14 00:30:00

df['DateTime']=df['DateTime'].agg(JalaliDate)
    #Out[35]: 
#0         1394-07-23
#1         1396-11-22
#2         1395-03-25

# 6) When was the first purchase in the data? When was the last one?'
df['DateTime_CartFinalize'].max()
    # '9/9/18 9:54'

df['DateTime_CartFinalize'].min()
    # '1/1/14 19:52'

# 7) The columns 'ID_Item' and 'ID_Customer' show the IDs of the sold items and customers, respectively.'
'# 7-1) How many unique items have been sold?
A=np.unique(df['ID_Item'])
len(A)   
	# Out[43]: 95232

#df['ID_Item'].value_counts().unique()
len(df['ID_Item'].value_counts())
    # Out[45]: 95232

'# 7-2) How many unique customers have bought items?
B=np.unique(df['ID_Customer'])
len(B)
    # Out[52]: 151634

'# 8) The column 'city_name_fa' shows the name of the cities.'
# How many unique cities have been used in the dataset?
len(np.unique(df['city_name_fa']))
    #Out[54]: 906

'# 9) Count the number of transactions in the cities.'
     #Sort the results in a descending manner and show the first 20 cities. 
# groupby base on the column city_name
df2=df.groupby('city_name_fa')  
# count numbers of the orders df3 and df4 are for a same reason
df3=df2['ID_Order'].count() 
df4=df2.agg({'ID_Order':['count']})   

# descending Sort the numbers of the orders 
df5=df4.sort_values(('ID_Order','count'), ascending=False)
df6=df5.iloc[:20 , :]
df6
# تهران          108303
# مشهد             6024
# اصفهان           5992

'# 10) Use the same logic to count the number of transactions in each year.' 
# 10-1) To do this, you first need to extract the year from the elements of 'DateTime_CartFinalize’ column.
df['year']=pd.DatetimeIndex(df['DateTime_CartFinalize']).year
df.head
df['year']
# Out[110]: 
# 0         2015
# 1         2018
# 2         2016

# there is a second way to extract the years using function
def extYear(x):
    x=pd.Timestamp(x)
    year=(x).year
    return(year)
df['year']=df['DateTime_CartFinalize'].agg(extYear)

# 10-2) After generating a new column called ‘Year’, 
      #you can groupby the whole dataset based on Year and use the logic in the previous question.  
df7=df.groupby('year')
df7.count()
df8=df7['year'].count()
df8

# 11) We need to count the number of transactions for some cities and in some specific years.
   # We can groupby our dataset based on both cities and year of purchase.  
df9 = df.groupby(['city_name_fa' , 'year']).count()['ID_Order']
df9.get(['اصفهان', 'تهران'])

# 12) The column 'Quantity_item' gives you the number of items purchased in each transaction.
   # What are the quantity levels used in this dataset? (by quantity levels I mean numbers and not categorical levels) 
   # Use the logic in Questions 9 and 10 to see what the twenty mostly-used quantity levels are in the dataset.  
  df10 = df.groupby('Quantity_item').count()['ID_Order']
  df10=np.sort(df10)
  df10
  df11=df10[-20:]
  df11   

# 13) Use the same method in Question 11 to obtain Quantity levels used in different cities separately.
    # Get the information about ' 'رشت and ' .'مشهد'
 df12 = df.groupby(['city_name_fa' , 'Quantity_item']).count()['ID_Order']
 df12.get(['مشهد', 'رشت'])
   
# 14) We can use the same approaches in Questions 11 and 13 to obtain Quantity levels used in different years.
    #(You do not need to do that, but it would be helpful to try) 
 df13 = df.groupby(['Quantity_item' , 'year']).count()['ID_Order']
 df13
 
# 15) We would like to get some information about our customers. So, we need to, first, group by our dataset based on the column 'ID_Customer'.
    # The first question is that what is the number of times each customer has made a purchase? 
    # Use the same method you used in Questions 9 and 10.
  df14 = df.groupby('ID_Customer').count()['ID_Order']
  df14
  df15=np.sort(df14)
  df15=df15[-20:]

# 16) The 'ID_Item' column gives you the IDs for the items sold in Digikala.
    # We can use this column to see what are the most frequently sold items in the dataset. 
    #1 Please find twenty of the best sellers.   
    # Hint: use the 'ID_Item' column and apply the value_counts function to it. 
  df16 = df['ID_Item'].value_counts()
  df17= df16[:20]

# 17) This code will give you the top five items sold in each city.(This question is optional by highly recommended)  
    cities=df['city_name_fa'].unique()
    # find the cities
    b=dict() #define an empty dictionary.
    # A dictionary is similar to a list only that each element can have a name in a dictionary Write a for loop to: 
    #Write a for loop to:
  # 1) Get each city as x :
  # 2) Call the ID_Item column 
  # 3) Count the number of items sold in each of these cities 
  # 4) Get only the first five IDs
  for x in cities:
       b[x]=df.groupby('city_name_fa').get_group(x)['ID_Item'].value_counts().index[:5]
      
        b['تهران']
#        Int64Index([294942, 36871, 51778, 45121, 8289], dtype='int64')
        b['اصفهان'] 
#        Int64Index([294942, 45121, 51778, 36871, 8289], dtype='int64') 
        b['مهاباد'] 
#        Int64Index([510718, 259039, 497985, 54850, 265540], dtype='int64') 
        

  for x in cities:
       b[x]=df.groupby('city_name_fa').get_group(x)['ID_Item'].value_counts()

b['مهاباد']
  # 153212    1
  # 41389     1
  # 130735    1
  # 721072    1
  # 82945     1
  # Name: ID_Item, Length: 110, dtype: int64

  for x in cities:
       b[x]=df.groupby('city_name_fa').get_group(x)['ID_Item'].unique()

 b['مهاباد']
#    Out[169]: 
#    array([  74927,   64842, 1096816,  814131,    9717,  572303,  557699,
#            863169,   10376,   10050,   87426,   91623,  349078,  267545,
#           781253,  245025,  732139,  134408,   43719,  717539,  290722, ...   
 
 for x in cities:    
      b[x]=df.groupby('city_name_fa').get_group(x)['year'].value_counts()

 b['مهاباد']     
#   Out[174]: 
#    2018    45
#    2017    27
#    2016    22
#    2015     8
#    2014     6
#    2013     2
#    Name: year, dtype: int64

 for x in cities:    
      b[x]=df.groupby('city_name_fa').get_group(x)['ID_Customer'].value_counts()

 b['مهاباد']     
#    Out[176]: 
#    472869     10
#    1105537     3
#    778089      2
#    3191724     2
#    Name: ID_Customer, Length: 93, dtype: int64



