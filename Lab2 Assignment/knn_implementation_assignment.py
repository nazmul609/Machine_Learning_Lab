# -*- coding: utf-8 -*-
"""
Created on Wed May  4 10:33:49 2022

@author: Nazmul
"""

## complete na

import numpy as np


class knn_classifier():
    
        
    def Calculate_Euclid_distance(self, training_points, testing_points):
        
        dist = 0
        for i in range (len(training_points)-1):
            dist = dist + (training_points[i] - testing_points[i])**2
            
        euclid_dist = np.sqrt(dist)
        return euclid_dist
    
    def nearnest_neighbor(self, X_train, test_data, k):
        
        distance_list = []
        
        for training_data in X_train:
            distance = self.Calculate_Euclid_distance(training_data, test_data)
            distance_list.append(( training_data, distance ))
        
        distance_list.sort(key=lambda x:x[1])
        
        
        
        neighbors_list = []
        
        for i in range(k):
            neighbors_list.append(distance_list[i][0])
            
        return neighbors_list
    
    
    def predict(self, X_train, test_data, k):
        
        neighbors = self.nearnest_neighbor(X_train, test_data, k)
        
        for data in neighbors:
            labels = []
            labels.append(data[-1])
            
        predicted_class = max(set(labels), key = labels.count)
        
        return predicted_class
        
        
##################################################################        
        
# testing with diabetes dataset       

import pandas as pd
from sklearn.model_selection import train_test_split


data_set = pd.read_csv(r'C:\Users\Nazmul\Desktop\diabetes.csv')        
        
x = data_set.drop(columns='Outcome', axis=1) 
y = data_set['Outcome']

x = x.to_numpy()
y = y.to_numpy()

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.2, random_state = 42)
x_train = np.insert(x_train, 8, y_train, axis=1)



classifier = knn_classifier()
x_test_size = x_test.shape[0]
y_pred = []

for i in range(x_test_size):
  prediction = classifier.predict(x_train, x_test[i], k=5)
  y_pred.append(prediction)
  
  
from sklearn.metrics import accuracy_score

accuracy = accuracy_score(y_test, y_pred)
print(accuracy*100)
        
        
        
        
        
        
    