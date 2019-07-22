'''
Title     : Set .union() Operation
Subdomain : Sets
Domain    : Python3
Author    : Alok Ranjan Bhoi
Created   : 22 July 2019
Problem   : https://www.hackerrank.com/challenges/py-set-union/problem
'''
n = input()
eng = set(map(int,input().split()))
b = input()
fre = set(map(int,input().split()))
print(len(eng.union(fre)))
