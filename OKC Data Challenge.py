#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: amolakkumar
"""

import pandas as pd

# Load in data
df = pd.read_csv('shots_data.csv')

# Split data by team
dfA = df[df['team'] == "Team A"]
dfB = df[df['team'] == "Team B"]

# Filter NC3 for Team A
dfANC3 = dfA[abs(dfA['y']) > 7.8]
dfANC3 = dfANC3[abs(dfANC3['x']) >= 23.75]

# Filter C3 for Team B
dfAC3 = dfA[abs(dfA['y']) <= 7.8]
dfAC3 = dfAC3[abs(dfAC3['x']) >= 22]

# Filter NC3 for Team B
dfBNC3 = dfB[abs(dfB['y']) > 7.8]
dfBNC3 = dfBNC3[abs(dfBNC3['x']) >= 23.75]

# Filter C3 for Team B
dfBC3 = dfB[abs(dfB['y']) <= 7.8]
dfBC3 = dfBC3[abs(dfBC3['x']) >= 22]

# Shot Distributions

ANC3 = (dfANC3.shape[0]/dfA.shape[0])*100
AC3 = (dfAC3.shape[0]/dfA.shape[0])*100

BNC3 = (dfBNC3.shape[0]/dfB.shape[0])*100
BC3 = (dfBC3.shape[0]/dfB.shape[0])*100

A2 = ((dfA.shape[0] - dfANC3.shape[0] - dfAC3.shape[0])/dfA.shape[0])*100

B2 = ((dfB.shape[0] - dfBNC3.shape[0] - dfBC3.shape[0])/dfB.shape[0])*100


# To get # of FGM for each team
dfAM = dfA[dfA['fgmade'] == 1]
dfBM = dfB[dfB['fgmade'] == 1]

# To get # of each type of 3 made for each team
dfANC3PM = dfANC3[dfANC3['fgmade'] == 1]
dfAC3PM = dfAC3[dfAC3['fgmade'] == 1]

dfBNC3PM = dfBNC3[dfBNC3['fgmade'] == 1]
dfBC3PM = dfBC3[dfBC3['fgmade'] == 1]

# To get # of 2PM for each team

A2PM = dfAM.shape[0] - dfANC3PM.shape[0] - dfAC3PM.shape[0]
B2PM = dfBM.shape[0] - dfBNC3PM.shape[0] - dfBC3PM.shape[0]

# Effective FG%

eFGA2 = A2PM/(dfA.shape[0] - dfANC3.shape[0] - dfAC3.shape[0])
eFGAC3 = (dfAC3PM.shape[0] + 0.5*(dfAC3PM.shape[0]))/dfAC3.shape[0]

eFGB2 = B2PM/(dfB.shape[0] - dfBNC3.shape[0] - dfBC3.shape[0])
eFGBC3 = (dfBC3PM.shape[0] + 0.5*(dfBC3PM.shape[0]))/dfBC3.shape[0]

