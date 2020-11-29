# -*- coding: utf-8 -*-
"""
Created on Tue Oct 20 13:20:55 2020

@author: Rahul
"""

import numpy as np
import pandas as pd
import matplotlib as plt

datA=pd.read_csv("C:\\Users\\Rahul\\Downloads\\mba.csv")

datA.describe()
datA.columns
datA.head(11)
data.tail(6)
data.iloc[49,:]
data.iloc[100:105,:]
data.iloc[:,2]
