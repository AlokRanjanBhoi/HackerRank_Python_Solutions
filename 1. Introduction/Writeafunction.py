'''
Title     : Write a function
Subdomain : Introduction
Domain    : Python3
Author    : Alok Ranjan Bhoi
Created   : 14 January 2019
'''
def is_leap(year):
    leap = False
    if (year % 400 == 0):
        leap = True
    elif year % 4 == 0 and year % 100 !=0:
        leap = True    
    return leap
