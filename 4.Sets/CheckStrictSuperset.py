'''
Title     : Check Strict Superset
Subdomain : Sets
Domain    : Python3
Author    : Alok Ranjan Bhoi
Created   : 17 July 2019
Problem   : https://www.hackerrank.com/challenges/py-check-strict-superset/problem
'''
A  = set(input().split())
n = int(input())
check = True
for i in range(n):
    s = set(input().split())
    if (s&A != s) or (s == A):
        check = False
        break
print(check)
