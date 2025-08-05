# -*- coding: utf-8 -*-
"""
Created on Sun Jun 25 09:10:17 2023

@author: user
"""
favorite_places = {
    
        'arjun' : [ 'shaymoly','karfa','farmgat'],
        
    
    
        'nusrat' : ['hemayedpur','nilkhet','mahakhali'],
    
    
    
        'arina' : ['london','washingtown','dhaka'],
        
    
    
    }
for name, places in favorite_places.items():
    print(f"\n{name.title()}`s favorite places are : ")
    for place in places: 
        print(f"\t {place.title()}")
        
         
    
