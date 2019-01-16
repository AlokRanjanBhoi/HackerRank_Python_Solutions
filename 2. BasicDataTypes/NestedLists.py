'''
Title     : Nested Lists
Subdomain : Data Types
Domain    : Python3
Author    : Alok Ranjan Bhoi
Created   : 16 January 2019
'''
# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import OrderedDict

n=int(input())
ar={}
val_ar=[]
for i in range(0,n):
    tmp_name=input()
    tmp_marks=float(input())
    ar[tmp_name]=tmp_marks
    val_ar.append(tmp_marks)
  
set_val=set(val_ar)
val_ar=list(set_val)
val_ar.sort()
sec_mark=val_ar[1]
##print sec_mark    
final_ar=[]
for i in ar:
    if(sec_mark==ar[i]):
        final_ar.append(i)

final_ar.sort()
for i in final_ar:
    print(i)
