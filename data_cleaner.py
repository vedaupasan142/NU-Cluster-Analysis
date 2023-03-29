# -*- coding: utf-8 -*-
"""
Created on Tue Nov 15 10:51:10 2022

@author: hoson
"""

import pandas as pd
import numpy as np
world=pd.read_csv('data/World Indicators.csv')

world['Business Tax Rate']=world['Business Tax Rate'].str.rstrip("%").astype('float')/100
world['GDP'] = world['GDP'].str.replace(',', '')
world['GDP'] = world['GDP'].str.replace('$', '')
world['GDP']=world['GDP'].astype('float')
world['Health Exp/Capita']=world['GDP'].replace('$', '').astype('float')
regions=list(set(world["Region"]))
print(regions)
for i in range(len(world.columns.values)-2):
    for j in regions:
        world[world.columns.values[i]].loc[world["Region"]==j]=world[world.columns.values[i]].loc[world["Region"]==j].replace(np.NaN,world[world.columns.values[i]].loc[world["Region"]==j].median())
print(world.isnull().sum())    
world.to_csv('data/World Indicators-clean.csv')

