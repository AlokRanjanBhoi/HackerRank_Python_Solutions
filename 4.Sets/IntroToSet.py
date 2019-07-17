'''
Title     : Introduction to Sets
Subdomain : Sets
Domain    : Python3
Author    : Alok Ranjan Bhoi
Created   : 17 July 2019
Problem   : https://www.hackerrank.com/challenges/py-introduction-to-sets/problem
'''
n = input()
ar = map(int,input().split(' '))
ar=set(ar)
print(sum(ar) / len(ar))
