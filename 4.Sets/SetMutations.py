'''
Title     : Set Mutations
Subdomain : Sets
Domain    : Python3
Author    : Alok Ranjan Bhoi
Created   : 20 July 2019
Problem   : https://www.hackerrank.com/challenges/py-set-mutations/problem
'''
n = int(input())
a = set(map(int,input().split()))
N = int(input())
for i in range(N):
    cmd = input().split()
    opt = cmd[0]
    s = set(map(int,input().split()))
    if (opt == 'update'):
        a |= s
    elif (opt == 'intersection_update'):
        a &= s
    elif (opt == 'difference_update'):
        a -= s
    elif (opt == 'symmetric_difference_update'):
        a ^= s
print(sum(a))
