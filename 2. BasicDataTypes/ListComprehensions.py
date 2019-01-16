'''
Title     : List Comprehensions
Subdomain : Data Types
Domain    : Python3
Author    : Alok Ranjan Bhoi
Created   : 16 January 2019

'''
# Enter your code here. Read input from STDIN. Print output to STDOUT
x=int(input())
y=int(input())
z=int(input())
n=int(input())
print([ [i,j,k] for i in range(x+1) for j in range(y+1) for k in range(z+1) if i+j+k != n ])
