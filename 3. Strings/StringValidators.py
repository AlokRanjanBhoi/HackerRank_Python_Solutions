'''
Title     : String Validators
Subdomain : Strings
Domain    : Python3
Author    : Alok Ranjan Bhoi
Created   : 16 Februry 2019
Problem   : https://www.hackerrank.com/challenges/string-validators/problem
'''
# Enter your code here. Read input from STDIN. Print output to STDOUT
inputStr=input()
resalnum = False
resalpha = False
resdigit = False
reslower = False
resupper = False
for i in inputStr:
    if(i.isalnum()):
        resalnum=True
    if(i.isalpha()):
        resalpha=True
    if(i.isdigit()):
        resdigit=True
    if(i.islower()):
        reslower=True
    if(i.isupper()):
        resupper=True
    
print(resalnum)
print(resalpha)
print(resdigit)
print(reslower)
print(resupper)
