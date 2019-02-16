'''
Title     : sWAP cASE
Subdomain : Strings
Domain    : Python3
Author    : Alok Ranjan Bhoi
Created   : 16 Februry 2019
Problem   : https://www.hackerrank.com/challenges/swap-case/problem
'''
__author__ = 'arsho'
def swap_case(s):
    newstring = ""
    
    for item in s:
        if item.isupper():
            newstring += item.lower()
        else:
            newstring += item.upper()
            
    return newstring
