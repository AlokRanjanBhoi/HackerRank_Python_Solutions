'''
Title     : Check Subset
Subdomain : Sets
Domain    : Python3
Author    : Alok Ranjan Bhoi
Created   : 17 July 2019
Problem   : https://www.hackerrank.com/challenges/py-check-subset/problem
'''
for i in range(int(input())): #More than 4 lines will result in 0 score. Blank lines won't be counted. 
    a = int(input()); A = set(input().split()) 
    b = int(input()); B = set(input().split())
    print((A & B) == A)
