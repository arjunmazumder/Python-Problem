# -*- coding: utf-8 -*-
"""
Created on Sun Jun 25 23:53:11 2023

@author: user
"""

cities = {
    'dhaka':{
        'capital':'dhaka is the capital of Bangladesh',
        'area': 'it`s total area is 306.38 square kilometres(119.29 mi)',
        'population':'the current population of dhaka is 23,210,000',
        'famous':'it`s famous for mosques and muslin',
        },
    'new delhi':{
        'capital':'new delhi is the capital of India ',
        'area':'it`s total area is 1,438 square kilometers (16.5  mi)',
        'population':'the current population of delhi is 32,066,000',
        'famous':'it`s famous for red fort, india gate, qutub minar',
        },
    'washington':{
        'capital':'washington d.c is the capital of U.S.A',
        'area':'it`s total area is 184,827 square kilometers(95.31 mi)',
        'population':'the current population of washington is 7.739 M',
        'famous':'it`s famous for the white house and rock creek park',
        },
    }
for citi_name, citi_information in cities.items():
    print(f"\ncity name : {citi_name.title()}")
    about_city = f"{citi_information['capital']}. {citi_information['area']}. {citi_information['population']}. {citi_information['famous']}."
    print(f"\tInformation of {citi_name.title()} : {about_city.title()}")