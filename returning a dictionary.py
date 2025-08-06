# -*- coding: utf-8 -*-
"""
Created on Sun Sep 10 02:08:36 2023

@author: user
"""

def build_person(first_name, last_name):
    person = {'first':first_name, 'last': last_name}
    return person
musician = build_person('arjun','mazumder')
print(musician)
