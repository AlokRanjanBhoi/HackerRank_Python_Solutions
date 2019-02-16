'''
Title     : Text Wrap
Subdomain : Strings
Domain    : Python3
Author    : Alok Ranjan Bhoi
Created   : 16 Februry 2019
Problem   : https://www.hackerrank.com/challenges/text-wrap/problem
'''
import textwrap
s = input()
w = int(input().strip())
print(textwrap.fill(s,w))
