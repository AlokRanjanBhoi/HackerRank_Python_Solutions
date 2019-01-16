'''
Title     : Tuples
Subdomain : Data Types
Domain    : Python3
Author    : Alok Ranjan Bhoi
Created   : 16 January 2019
'''
# Enter your code here. Read input from STDIN. Print output to STDOUT
n=int(input())
numbers=input().strip().split()
ar=[]
for i in range(0,len(numbers)):
   ar.append(int(numbers[i]))
t=tuple(ar)
print(hash(t))
