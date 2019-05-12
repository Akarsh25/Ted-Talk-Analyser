# -*- coding: utf-8 -*-
"""
Created on Thu Apr 25 22:30:32 2019

@author: My Pc
"""
import ast
import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt

def networkRelated(dataset):
    dataset['related_talks'] = dataset['related_talks'].apply(lambda x: ast.literal_eval(x))
    s = dataset.apply(lambda x: pd.Series(x['related_talks']),axis=1).stack().reset_index(level=1, drop=True)
    s.name = 'related'
    related_dataset = dataset.drop('related_talks', axis=1).join(s)
    related_dataset['related'] = related_dataset['related'].apply(lambda x: x['title'])
    d = dict(related_dataset['title'].drop_duplicates())
    d = {value: key for key, value in d.items()}
    related_dataset['title'] = related_dataset['title'].apply(lambda x: d[x])
    related_dataset['related'] = related_dataset['related'].apply(lambda x: d[x])
    related_dataset = related_dataset[['title', 'related']]
    edges = list(zip(related_dataset['title'], related_dataset['related']))
    
    G = nx.Graph()
    G.add_edges_from(edges)
    plt.figure(figsize=(10, 10))
    nx.draw(G, with_labels=False,node_color='purple',node_size=10)