# -*- coding: utf-8 -*-
"""
Created on Wed May  4 10:02:50 2022

@author: Nazmul
"""

import numpy as np
import pandas as pd

from sklearn.model_selection import train_test_split
from matplotlib import pyplot as plt

from sklearn.neighbors import KNeighborsClassifier


data_set = pd.read_csv(r'C:\Users\Nazmul\Desktop\diabetes.csv')
data_set.head()
print("length of dataset:", len(data_set))
data_set.head()

x = data_set.iloc[:, 0:8 ] # features
y = data_set.iloc[:, 8 ]  # labels (0 or 1)

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.1, random_state = 42)

train_accuracy = []
test_accuracy = []

neighbors = range (1, 40)

for i in neighbors:
  KNN = KNeighborsClassifier( n_neighbors = i )
  KNN.fit( x_train, y_train )
  train_accuracy.append( KNN.score(x_train, y_train) )
  test_accuracy.append( KNN.score(x_test, y_test) )

plt.plot(neighbors, train_accuracy, label="training accuracy")
plt.plot(neighbors, test_accuracy, label="testing accuracy")
plt.xlabel("Number of Neighbors")
plt.ylabel("Accuracy")


error = []
for i in range(1,40):

  KNN = KNeighborsClassifier (n_neighbors=i)
  KNN.fit(x_train, y_train)
  pred_i = KNN.predict(x_test)
  error.append(np.mean(pred_i != y_test))
  #print(np.mean(pred_i != y_test))
  
  
  
plt.figure(figsize=(12,6))

plt.plot(range(1,40), error, color = 'red', linestyle='dashed', marker='o',
    markerfacecolor='blue', markersize=10)

plt.title("Error rate K value")
plt.xlabel("K value")
plt.ylabel("Mean Error")





