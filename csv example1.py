# (a) read the csv file in python
# (b) print name and regno of students having maximum marks in byod pratical 1

import pandas as pd
data=pd.read_csv('marks.csv')
pd.set_option('display.max_column',None)
print(data.head()) #first five
print(data.columns)
print(data)
##
pd.set_option('display precision',2)
print(data.describe())
## name and registration number of student having maximum marks in byod pratical
imporrt numpy as np
print (data[data.iloc[:,3].values==np.amax(data.iloc[:,3}.values)].iloc[:,0:3])
## name and registration number of student obtained total 70% or more
data['Total']=data['BYOD-practicall']+data['Test - code based1']
print(data.head())
print(data[data.iloc[:,6].values>=42].iloc[:,0,2])

##visualise the data of marks for byod pratical 1 and code based test 1
import matplotlib.pyplot as plt
plt.subplot(1,2,1)
plt.hist(data.iloc[:,3].values)
plt.subplot(1,2,2)
plt.hist(data.iloc[:,5].values)

plt.title('Test-code based')
plt.show()


## create dataframe for z
data1=pd.dataFrame(z)
data1.columns=['0-40','40-60','60-90','90-100']
data1.index=['BYOD-practical','TEST-code based']
print(data1)

## display % of marks obtained for BYOD &
