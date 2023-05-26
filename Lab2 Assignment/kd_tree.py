# -*- coding: utf-8 -*-
"""
Created on Mon May  9 20:19:34 2022

@author: Nazmul
"""

from binarytree import tree, Node
from math import floor
import pandas as pd

class KD_Tree:
    def __init__(self, data):
        self.data = data
        self.tree = None
        
    def build(self, points, depth):
        k = len(points.columns)
        axis = depth % k
        column = points.columns[axis] 
        
        if len(points) == 0:
            return None
        
        points_list = points.sort_values(by= [column], ascending= True)
        
        if len(points_list) % 2 ==0:
            median_index = int( (len(points_list)/2) )
        else:
            median_index = floor( (len(points_list)/2) )
            
        node = Node(round( points_list.iloc[median_index][column]), 3)
        node.left = self.build( points_list.iloc[0:median_index], depth+1)
        node.right = self.build( points_list.iloc[median_index+1:], depth+1)
        
        return node
    
    
    
    def KD_Tree_Implementation(self):
        self.tree = self.build(self.data, depth=0)    
    


data_points = pd.DataFrame(data=[[2,3],[5,4],[9,6],[4,7],[8,1],[7,2]], columns=["X","Y"])    

KD = KD_Tree(data_points)
KD.KD_Tree_Implementation() 
  

 
    
    
    
    
    
    
    