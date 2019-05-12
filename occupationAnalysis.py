# -*- coding: utf-8 -*-
"""
Created on Thu Apr 25 22:27:47 2019

@author: My Pc
"""
import matplotlib.pyplot as plt
import seaborn as sns

def occupationAnalysis(dataset):
    print(dataset["speaker_occupation"].value_counts().head(10),"\n")
    
    
    #printing the top 5 occupation's number of views.
    print("Writer: ",int(dataset[dataset["speaker_occupation"]=="Writer"]["views"].sum() / len(dataset[dataset["speaker_occupation"]=="Writer"])))
    print("Designer: ", int(dataset[dataset["speaker_occupation"]=="Designer"]["views"].sum() / len(dataset[dataset["speaker_occupation"]=="Designer"])))
    print("Artist: ",int(dataset[dataset["speaker_occupation"]=="Artist"]["views"].sum() / len(dataset[dataset["speaker_occupation"]=="Artist"])))
    print("Jornalist: ",int(dataset[dataset["speaker_occupation"]=="Journalist"]["views"].sum() / len(dataset[dataset["speaker_occupation"]=="Journalist"])))
    print("Entrepreneur",int(dataset[dataset["speaker_occupation"]=="Entrepreneur"]["views"].sum() / len(dataset[dataset["speaker_occupation"]=="Entrepreneur"])))
    
    occupation_df = dataset.groupby('speaker_occupation').count().reset_index()[['speaker_occupation', 'comments']]
    occupation_df.columns = ['occupation', 'appearances']
    occupation_df = occupation_df.sort_values('appearances', ascending=False)
    plt.figure(figsize=(15,5))
    sns.barplot(x='occupation', y='appearances', data=occupation_df.head(10))
    plt.show()