'''
Title     : Set .discard(), .remove() &amp; .pop()
Subdomain : Sets
Domain    : Python3
Author    : Alok Ranjan Bhoi
Created   : 18 July 2019
Problem   : https://www.hackerrank.com/challenges/py-set-discard-remove-pop/problem
'''
n = int(input())
s = set(map(int, input().split())) 
n = int(input())
for i in range(n):
    cmd = list(input().split(' '))
    if (len(cmd) == 1):
        s.pop()
    else:
        value = int(cmd[1])
        s.discard(value)
print(sum(s))
