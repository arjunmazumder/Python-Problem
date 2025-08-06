# -*- coding: utf-8 -*-
"""
Created on Sat Jun 24 22:30:44 2023

@author: user
"""

users = {
    
    'arjumazumder2' : {
        'first_name' : 'arjun',
        'last_name' : 'mazumder',
        'location' : 'karfa',
        
        },
    'ahkishil202' : {
        'first_name' : 'ahki',
        'last_name' : 'shil',
        'location' : 'madhra',
        },
    
    }
for username, user_information in users.items(): 
    print(f" username : {username} ")
    full_name = f"{user_information['first_name']} {user_information['last_name']} "
    location = user_information['location']
    print(f"\tFull name : {full_name.title()}")
    print(f"\tLocation : {location.title()}")
    
    
    
    