# -*- coding: utf-8 -*-
"""
Created on Sat Apr 20 23:09:48 2019

@author: My Pc
"""
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

def knn(dataset,comments,views,languages):    
    #split dataset
    r_fb=[]
    #neg_descriptors = {"Confusing", "Unconvincing", "Longwinded", "Obnoxious", "OK"}
    dataset['ratings'] = dataset['ratings'].apply(lambda x: eval(str(x)))
    for i in range(len(dataset['ratings'])):
         if dataset['comments'][i]<100 and dataset['views'][i]<500000 and dataset['languages'][i]<30:
            r_fb.append(0)
         else:
            r_fb.append(1)

    dataset['r_feedback']=r_fb
    X=dataset[['comments','views','languages']]
    Y=dataset['r_feedback']
    
    # Split data into training and testing sets
    X_train,X_test,y_train,y_test = train_test_split(X,Y,random_state=0,test_size=0.5)
    
    #Instantiate the model with 5 neighbors
    classifier=KNeighborsClassifier(algorithm='brute',n_neighbors=10)
    
    #Fit the model on the training data
    classifier.fit(X_train,y_train)
    
    #See how the model performs on the test data.
    print("Accuracy score of the algorithm is:",classifier.score(X_test,y_test)*100)
    
    #prediction results based on input data
    prediction = classifier.predict([[comments,views,languages]])
    if(prediction[0]==1):
        print("Talk will receive positive feedback")
    else:
        print("Talk will receive negative feedback")
