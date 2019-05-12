# -*- coding: utf-8 -*-
"""
Created on Sat Apr 20 22:32:28 2019

@author: My Pc
"""
import numpy as np
import matplotlib.pyplot as plt
def ratingsPlot(dataset,counter,neg_descriptors):
    dataset['ratings'] = dataset['ratings'].apply(lambda x: eval(str(x)))
    for i in range(len(dataset['ratings'])):
        x,y=0,0
        for j in range(len(dataset['ratings'][i])):
            counter[dataset['ratings'][i][j]['name']] += dataset['ratings'][i][j]['count']
            if dataset['ratings'][i][j]['name'] in neg_descriptors:
                y+=dataset['ratings'][i][j]['count']
            else:
                x+=dataset['ratings'][i][j]['count']
    frequencies = list(counter.values())
    #descr = counter.keys()
    descriptors = [x for _,x in sorted(zip(frequencies,counter.keys()), reverse=True)]
    neg_indices  = [x for x in range (len(descriptors)) if descriptors[x] in neg_descriptors]
    frequencies.sort(reverse=True)
    
    indices = np.arange(len(descriptors))
    bar = plt.bar(indices, frequencies, 0.8)
    [bar[i].set_color('r') for i in neg_indices]
    plt.xticks(indices, descriptors, rotation=45, ha="right")
    plt.show()