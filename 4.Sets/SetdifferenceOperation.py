'''
Title     : Set .difference() Operation
Subdomain : Sets
Domain    : Python3
Author    : Alok Ranjan Bhoi
Created   : 18 July 2019
Problem   : https://www.hackerrank.com/challenges/py-set-difference-operation/problem
'''
e = int(input())
eng = set(map(int,input().split())) 
f = int(input())
fre = set(map(int,input().split()))
print(len(eng - fre))
