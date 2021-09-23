#!/usr/bin/env python
# coding: utf-8

# In[89]:


import pandas as pd
import numpy as np


# In[90]:


## Reading in CSV file, all code written on Jupyter Notebook
player_data = pd.read_csv(r"C:\Users\rorym\fpl\Fantasy-Premier-League-master\data\2021-22\cleaned_players.csv")
player_data


# In[91]:


### DF info

player_data.shape
player_data.columns


# In[92]:


## DF Datatypes
player_data.dtypes


# In[93]:


### Aim is to find players with the most ict threat without the points to correspond with their allocated threat.
### I.E underperforming their threat expectation

## Making new column based on dividing a players total points versus their ICT rating. Looking for players with low points relative to their ICT so low figures are desirable in this colum
player_data['Total Points/ICT']= player_data['total_points']/player_data['ict_index']

## Removing negative/null figures
player_data_potential=player_data.loc[player_data['Total Points/ICT']>0]

## Replacing infinite figures with NaN caused by null on ICT index
player_data_potential.replace([np.inf, -np.inf], np.nan)

## Removing NA's
player_data_potential.dropna(subset = ['Total Points/ICT'])

## Sorting by lowest at top
player_data_potential=player_data_potential.sort_values('Total Points/ICT')

## Filtering for more than 10 points as subset shown limited to players who have 1 or 2 points
player_data_potential=player_data_potential.loc[player_data_potential['total_points'] > 10]

## Top 15 players with point potential for review
player_data_potential.head(15)

## As of week 5: Notable inclusions are Grealish,Mane,Sarr,Elyounoussi and GroB


# In[96]:


### Focusing on specific positions (GK/DEF/MID/FWD) to find an affordable transfer option

## Changing element_type to a string
player_data['element_type']=player_data['element_type'].astype('string')

## Transfer funds available = 4.9M and Position = DEF
player_data_transfer=player_data.loc[(player_data['now_cost']<=49) & (player_data['element_type']=='DEF')]

## Sorting by influence
player_data_transfer=player_data_transfer.sort_values('influence',ascending=False)
player_data_transfer

