# -*- coding: utf-8 -*-
"""
Created on Thu Jun 29 08:43:49 2023

@author: user
"""

sandwich_orders = ['chicken', 'egg', 'seafood', 'roast beef', 'grilled', 'ham','nutella' ]
finished_sandwiches = []
while sandwich_orders:
    sandwich = sandwich_orders.pop()  
    print(f" I made your {sandwich.title()} sandwich.")   
    finished_sandwiches.append(sandwich)
    
    
for finished_sandwiche in finished_sandwiches:
    print(finished_sandwiche)
print("All chicken was made.")
    
    
    
    