# -*- coding: utf-8 -*-
"""
Created on Sat Apr 20 17:56:24 2019

@author: My Pc
"""

import pandas as pd
import datetime
import pubYearPlot as pyp
import tagsTalksPlot as ttp
import ratingsPlot as rp
import knn as k
import occupationAnalysis as oa
import networkRelated as np



pd.set_option('display.max_columns',50)
pd.set_option('display.expand_frame_repr', False)
dataset=pd.read_csv('ted_main.csv') 

#formatting date
dataset['film_date'] = dataset['film_date'].apply(lambda x: datetime.datetime.fromtimestamp( int(x)).strftime('%d-%m-%Y'))
dataset['published_date'] = dataset['published_date'].apply(lambda x: datetime.datetime.fromtimestamp( int(x)).strftime('%d-%m-%Y'))
dataset["published_year"] = dataset["published_date"].apply(lambda x: x.split("-")[2])

dataset = dataset.sort_values('views', ascending=False)

print("Plotting graph based on number of talks published each year\n")
pyp.pubYearPlot(dataset)


print("Occupation Analysis:\n")
oa.occupationAnalysis(dataset)


#plotting views for each tag.
print("\nGraph on views based on different tags\n")
ttp.tagsTalksPlot(dataset)

#tags count yearly (CAN USE GUI HERE)
print("\nFor 2015\n")
year="2015"
ttp.tagsCountYearly(dataset,year)
print("\nFor 2016\n")
year="2016"
ttp.tagsCountYearly(dataset,year)
print("\nFor 2017\n")
year="2017"
ttp.tagsCountYearly(dataset,year)

#Ratings vs count plot
counter = {'Funny':0, 'Beautiful':0, 'Ingenious':0, 'Courageous':0, 'Longwinded':0, 'Confusing':0, 'Informative':0, 'Fascinating':0, 'Unconvincing':0, 'Persuasive':0, 'Jaw-dropping':0, 'OK':0, 'Obnoxious':0, 'Inspiring':0}
neg_descriptors = {"Confusing", "Unconvincing", "Longwinded", "Obnoxious", "OK"}
rp.ratingsPlot(dataset,counter,neg_descriptors)

print("\nEnter details for predicting if the talk will receive positive or a negative feedback:\n")
x=input("Enter Number of comments received:\n")
#y=input("Enter duration in minutes:\n")
#z=input("Enter Number of languages:\n")
t=input("Enter Views:\n")
l=input("Languages count\n")
k.knn(dataset,x,t,l)

print("Network graph for related talks for each talk:\n")
np.networkRelated(dataset)


