#! /Users/sanjaymsanthosh/anaconda/anaconda3/bin/python3
import os
import pandas as pd
import json

dataset_base = os.path.join(os.getcwd(),'..','dataset')

# datasets used : 

# English First Names
# https://data.world/axtscz/english-first-names
# List of first names from an English/American culture. 
# There are around 4,500 Female name and 1,500 Male names 

# First Names
# https://data.world/axtscz/english-first-names
# 7.000 first names CSV. (also known as baby-names by soon to be parents)

ENF_path = os.path.join(dataset_base,'ENGivenFemale.json')
BNC_path = os.path.join(dataset_base, 'babynames-clean.csv')


with open(ENF_path) as file:
    ENF = json.load(file)
BNC = pd.read_csv(BNC_path)

# Combining data to one file
data = pd.DataFrame(columns=['Name' , 'Gender'])
names = set()

# boy :1
# girl :0
print('Processing BNC File')
for indx,val in enumerate(BNC.itertuples()): 
    if(indx%1000==0):print(indx,end = '  ')
    name,gender = val[1].lower(),0 if val[2]=='girl' else 1
    if(name in names):continue
    names.add(name)
    data = data.append({'Name':name , 'Gender':gender},True)

print('\n\nProcessing ENF File')
for indx,item in enumerate(ENF):
    if(indx%1000==0):print(indx,end = '  ')
    name,gender = item['name'].lower(),1 if item['gender']=='M' else 0
    if(name in names):continue
    names.add(name)
    data = data.append({'Name':name , 'Gender':gender},True)

print('\n\n\tSUMMARY\n','.'*50)
print(data.head(),'\n')
print(data.describe(),'\n')
print(data.info(),'\n')

print('\tSaving to CSV ....')
data.to_csv(os.path.join(dataset_base,'Names.csv'))
print('\n\t PROCESS COMPLETED')


