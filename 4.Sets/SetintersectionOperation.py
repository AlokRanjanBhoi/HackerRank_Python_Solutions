'''
Title     : Set .intersection() Operation
Subdomain : Sets
Domain    : Python3
Author    : Alok Ranjan Bhoi
Created   : 20 July 2019
Problem   : https://www.hackerrank.com/challenges/py-set-intersection-operation/problem
'''
e = int(input())
eng = set(map(int,input().split()))
f = int(input())
fre = set(map(int,input().split()))
print(len(eng & fre))
