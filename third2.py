from matplotlib.pyplot import axis
import pandas as pd
import numpy as np

"""
print(pd.__version__)
#create a Series
s=pd.Series([1,3,5,np.nan,6,8])
print(s)
#create a Series from an array
data=np.array(['a','b','c','d'])
s=pd.Series(data)
print(s)
#create a Series from a dict
data1={'a':0., 'b':1., 'c':2.}
s=pd.Series(data1)
print(s)

#creating a DatFrame from dict of Series or dicts 
df=pd.DataFrame(np.random.randn(7,4), index=[2,3,4,5,6,7,8], columns=list('ABCD'))
print(df)
df1=pd.DataFrame({
    'A':1.,
    'B':pd.Timestamp('20200102'),
    'C':pd.Series(1,index=list(range(4)), dtype='float32'),
    'D':np.array([3]*4,dtype='int32'),
    'E':pd.Categorical(["test","train","test","train"]),  #Categoricals can only take on only a limited and usually 
    'F':"foo"
})
print(df1)
data2=np.arange(300).reshape(60,5)
df2=pd.DataFrame(data2)
print(df2.head(3)) #returns the first 'n' rows for the object based on position and its used to quickly test if object has the right type of data in it 
print(df2.tail(3)) #returns last 'n' rows from the object based on position and is used to quickly verify data after sorting or appending rows

df3=pd.DataFrame(np.random.randn(7,4), index=['a','b','c','d','e','f','g'], columns=list('ABCD')) #create random numbers as values
print(df3.index) #outputs the values of index
print(df3.columns) #outputs the columns of the dataframe
print(df3.values) #outputs values of arrays

df4=pd.DataFrame(np.random.randn(6,4), index=list('abcdef'), columns=list('ABCD'))
print(df4.loc[['a','b','d'], :]) #raises KeyError when the items are not found
print(df4.iloc[[0, 1, 3], :]) #raises IndexError if a requested indexer is out-of-bounds, exceptslice indexers which allow out-of-bounds indexing.

print(df4.count()) #number of non-NA observations
print(df4.mean()) #mean of values
print(df4.std()) #Bessel-corrected sample standard version
print(df4.sum()) #sum of values
print(df2.describe())#it computes a variety of summary statistics about a Series or the columns of a DataFrameexcluding NAs
"""
data3=np.arange(30).reshape(6,5)
df5=pd.DataFrame(data3, index=['a','b','c','d','e','f'], columns=['A','B','C','D','E'])
print(df5)
a=df5.drop(['a'], axis=0) #delete rows
print(a)
b=df5.drop(['A'], axis=1) #delete columns
print(b)
c=b.append(a) #append rows of other to the end of caller returning a new object
df5=pd.concat(data3, index=['a','b','c','d','e','f'], columns=['A','B','C','D','E'])
c=b.append(a)
print(c)

#conforms data to match a given set of labels along a particular axis
s=pd.Series(np.random.randn(5), index=['a','b','c','d','e'])
print(s)
print(s.reindex(['e','b','f','d']))
new_index=['e','d','ghi','kil']
print(s.reindex(new_index))

#iterating over DataFrame columns returnng a tuple with the column name and the content as a Series
df6=pd.DataFrame(np.random.randn(4,3), columns=['A','B','C'])
print(df6)
i=1
for s in df6.iteritems():
    print("column: %d value: %s"%(i,s))
    i+=1
s=pd.Series([1,2,3,4,5,4])
print(s.pct_change()) #computes percentage change over a given number of periods by using fill_method to fill NA/null values before computing
s1=pd.Series(np.random.randn(1000))
s2=pd.Series(np.random.randn(1000))
print(s1.cov(s2)) #computes covariance between series
frame=pd.DataFrame(np.random.randn(1000,5), columns=['a','b','c','d','e'])
print(frame.cov()) #computes covariance between dataframes

#sorting
df7=pd.DataFrame({
    'one':pd.Series(np.random.randn(3), index=['a','b','c']),
    'two':pd.Series(np.random.randn(4), index=['a','b','c','d']),
    'three':pd.Series(np.random.randn(3), index=['b','c','d']),
})
unsorted_df=df7.reindex(index=['d','a','c','b'], columns=['three','two','one'])
print(unsorted_df)
print(unsorted_df.sort_index()) #sort pandas object by its index values
print(unsorted_df.sort_index(ascending=False)) #sort pandas object by its index values when ascending is false

df8=pd.DataFrame({
    'one':[2,1,1,1],
    'two':[1,3,2,4],
    'three':[5,4,3,2]
    })
print(df8.sort_values(by='two')) #sort a Series by its values 
df9=pd.DataFrame(np.random.randn(5,3), index=['a','c','e','f','h'], columns=['one','two','three'])
df9=df9.reindex(['a','b','c','d','e','f','g','h'])
print(df9)
print(df9['one'].isna()) #detect missing values
print(df9.sum(axis=1)) #NA values are treated as zero
dff=pd.DataFrame(np.random.randn(10,3), columns=list('ABC'))
dff.iloc[3:5, 0]=np.nan
dff.iloc[4:6, 1]=np.nan
dff.iloc[5:8, 2]=np.nan
print(dff)
print(dff.mean())
print(dff.fillna(dff.mean())) # fill-in NA values with non-NA data by replace NA with a scalar value
print(dff.mean())
print(dff.dropna()) #deletes axis labels with missing data












