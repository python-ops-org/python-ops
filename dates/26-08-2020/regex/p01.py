


import pandas as pd
import numpy as np


"""
#Example-1
#create a series from ndarray
#index taken by default
d = np.array(['Aws', 'Azure', 'GCP', 'OPENSTACK' ])
s = pd.Series(d)
print(s)

"""

"""
#Example-2
#index will be passed

d = np.array(['AWS', 'AZURE', 'GCP', 'OPENSTACK'])
s = pd.Series(d,index=[100,101,102,103])
print(s)

"""
"""
d = {'cloud1': "aws", 'cloud2': 'azure'}
s = pd.Series(d)
print(s)

"""

"""

d = {'1': "aws", '2': 'azure'}
s = pd.Series(d, index=['1', '2','3'])
print(s)
"""

"""
#Retrieve multiple elements using a list of index label values.

s = pd.Series([1,2,3],index = ['a','b','c'])

#retrieve multiple elements
print(s[['a','b','c']])

"""

"""
#Accessing Data from Series with Position

import pandas as pd
s = pd.Series([1,2,3],index = ['a','b','c'])
print(s[2])
"""
