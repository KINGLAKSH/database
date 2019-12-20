"""
Code Challenge
  Name: 
    Thanks giving Analysis
  Filename: 
    Thanksgiving.py
  Problem Statement:
    Read the thanksgiving-2015-poll-data.csv file and 
    perform the following task :
"""

#Importing the requrired Libraries 
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#Opening the file and assigning the whole data
data = pd.read_csv("D:\\Study/Database_with_python\\New folder\\thanksgiving-2015-poll-data.csv")
#Making a dublicate dataframe
real = pd.read_csv("D:\\Study/Database_with_python\\New folder\\thanksgiving-2015-poll-data.csv")


"""
    Convert the column name to single word names
"""
'''
cols = list(data.columns.values)
new = []
for i in range(0,65):   
    new.append("col"+str(i))
dict1={}
for i in range(0,len(new)):
    dict1[cols[i]] = new[i]

data.rename(columns=dict1, inplace=True) 
'''



"""    
    Using the apply method to Gender column to convert Male & Female
"""

data['col62']=data['col62'].apply(lambda x : 0 if (x == 'Male') else 1).head(10)	

"""
    Using the apply method to clean up income    
    (Range to a average number, X and up to X, Prefer not to answer to NaN)
"""
data['col63'] = data['col63'].astype(str)

data['col63'] = data['col63'].replace('Prefer not to answer',np.nan)

def income(sal):
    if 'to' in str(sal):
        sal = sal.replace('$','')
        sal = sal.replace(',','')
        a,b = sal.split(' to ')
        return((float(a)+float(b))/2)
    elif('$200,000 and up'):
        return int(200000)

data['col63'] = data['col63'].apply(income)   







"""    
    compare income between people who tend to eat homemade cranberry sauce for
    Thanksgiving vs people who eat canned cranberry sauce?
"""
homemade =(data[data['col8']=='Homemade']['col63']).mean()
canned =(data[data['col8']=='Canned']['col63']).mean()

#data['col8'] = data['col8'].astype(str)
#data['col8']=data['col8'].replace('Other (please specify)',np.nan)
#data['col8']=data['col8'].replace('None',np.nan)
#
#data['col9'] = data['col9'].astype(str)
#
##dict1={}
##for i in range(0,len(new)):
##    dict1[cols[i]] = new[i]
#for i in data['col8']:
#    if(i==np.nan):
#        i = i.replace(i,)
#    else:
#        pass
#        
plt.xticks([0,1],['Homemade','Canned'])
plt.bar([0,1],[homemade,canned],color=['red','green'])
plt.show()



"""    
    find the average income for people who served each type of cranberry sauce
    for Thanksgiving (Canned, Homemade, None, etc).Plotting the results of aggregation
"""
data['col8'].value_counts()
homemade =(data[data['col8']=='Homemade']['col63']).mean()
canned =(data[data['col8']=='Canned']['col63']).mean()
none =(data[data['col8']=='None']['col63']).mean()
others =(data[data['col8']=='Other (please specify)']['col63']).mean()


plt.pie([homemade,canned,others,none],labels=['Homemade','Canned','Other (please specify)','None'],autopct='%1.1f%%',
        shadow=True, startangle=90)
plt.show()






"""    
    Do people in Suburban areas eat more Tofurkey than people in Rural areas?
"""
Suburban = len(data[data['col60']=='Suburban']['col2'])
Rural = len(data[data['col60']=='Rural']['col2'])

plt.xticks([0,1],['Suburban','Rural'])
plt.bar([0,1],[Suburban,Rural],color=['red','green'])
plt.show()





"""
    Where do people go to Black Friday sales most often?
"""

black_fri_values = data[data['col57']=='Yes']['col64'].value_counts().tolist()
black_fri_names = data[data['col57']=='Yes']['col64'].unique().tolist()

black_fri_names.pop()

black_fri_names = tuple(black_fri_names) 
# lets plot 
plt.pie(black_fri_values,labels=black_fri_names)


"""
    Is there a correlation between praying on Thanksgiving and income?
"""
#Taking The mean
YesPray = data[data['col51']=='Yes']['col63'].mean()
NotPray = data[data['col51']=='No']['col63'].mean()

#Ploting the chart
plt.pie([YesPray,NotPray],labels=['Who Pray','Who Not Pray'],autopct='%1.1f%%',shadow=True, startangle=90)

"""
    What income groups are most likely to have homemade cranberry sauce?
"""
Incomes = data[data['col8']=='Homemade']['col63'].value_counts().tolist()
valueincome = tuple(data[data['col8']=='Homemade']['col63'].unique())

plt.pie(Incomes,labels=valueincome)



"""
    Verify a pattern:
        People who have Turducken and Homemade cranberry sauce seem to have 
        high household incomes.
        People who eat Canned cranberry sauce tend to have lower incomes, 
        but those who also have Roast Beef have the lowest incomes
 """
#People who have Turducken and Homemade cranberry
Incomes1 = data[(data['col8']=='Homemade')&(data['col2']=='Turducken')]['col63'].mean()
#People who eat Canned cranberry sauce
Incomes2 = data[data['col8']=='Canned']['col63'].mean()
#People who eat Roast Beef
Incomes3 = data[data['col2']=='Roast beef']['col63'].mean()

#Ploting the graph
plt.xticks([0,1,2],['People who have Turducken and Homemade cranberry','People who eat Canned cranberry sauce','People who eat Roast Beef'])
plt.bar([0,1,2],[Incomes1,Incomes2,Incomes3],color=['red','green','blue'])
plt.show()





