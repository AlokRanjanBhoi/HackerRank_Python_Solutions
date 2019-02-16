'''
Title     : Mutations
Subdomain : Strings
Domain    : Python3
Author    : Alok Ranjan Bhoi
Created   : 16 Februry 2019
Problem   : https://www.hackerrank.com/challenges/python-mutations/problem
'''
# Enter your code here. Read input from STDIN. Print output to STDOUT
s=nput()
in_str_ar=input().strip().split()
pos=int(in_str_ar[0])
c=in_str_ar[1]
final_str=s[:pos]+c+s[pos+1:]
print(final_str)
