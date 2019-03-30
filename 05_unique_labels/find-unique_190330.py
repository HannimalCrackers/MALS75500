#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 30 08:29:21 2019

@author: hhouse
"""

import pandas as pd

# Load datasets as pandas dataframes
df_nyc = pd.read_csv("stage3_format_nyc.csv")
df_25pct = pd.read_csv("stage3_format_nyc_25pct.csv")

# Deleting unnecessary columns
del df_nyc['confidence']
del df_nyc['mid']
del df_25pct['confidence']
del df_25pct['mid']

print(df_nyc.columns)
print(df_25pct.columns)
#
df_unique_nyc = df_nyc[~df_nyc.label.isin(df_25pct.label)]
print(df_unique_nyc)

df_unique_25pct = df_25pct[~df_25pct.label.isin(df_nyc.label)]
print(df_unique_25pct)

print("NYC unique labels: " + str(df_unique_nyc['label'].nunique()))
print("NYC 25pct unique labels: " + str(df_unique_25pct['label'].nunique()))

# Saving out new dataframes to CSV
df_unique_nyc.to_csv('stage4_unique_nyc.csv')
df_unique_25pct.to_csv('stage4_unique_nyc_25pct.csv')