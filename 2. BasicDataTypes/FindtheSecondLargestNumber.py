'''
Title     : Find the Second Largest Number
Subdomain : Data Types
Domain    : Python3
Author    : Alok Ranjan Bhoi
Created   : 16 January 2019
'''
# Enter your code here. Read input from STDIN. Print output to STDOUT
n=int(input())
num_str_ar=input().strip().split()

num_ar=list(map(int,num_str_ar))
set_tmp=set(num_ar)
final_ar=list(set_tmp)
final_ar.sort()
print(final_ar[-2]
