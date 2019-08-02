'''
Title     : Iterables and Iterators
Subdomain : Itertools
Domain    : Python3
Author    : Alok Ranjan Bhoi
Created   : 2 August 2019
Problem   : https://www.hackerrank.com/challenges/iterables-and-iterators/problem
'''
from itertools import combinations
n = int(input())
ar = input().split()
k = int(input())
comb_list = list(combinations(ar,k))
a_list = [e for e in comb_list if 'a' in e]
print(len(a_list) / len(comb_list))
