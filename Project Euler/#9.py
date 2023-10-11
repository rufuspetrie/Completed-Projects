#!/bin/python
import sys
test_list=[]
t = int(raw_input().strip())
for a0 in xrange(t):
    n = int(raw_input().strip())
    test_list.append(n)
    
# Given a and n, we can compute b
def check(n):
    lst=[]
    for a in range(1,n):
        b=(a**2-(a-n)**2)/(2*(a-n))
        c=(a**2+b**2)**(0.5)
        if a+b+c==n and a>0 and b>0 and c>0:
            lst.append(int(a*b*c))
    if len(lst)>0:
        return max(lst)
    else: 
        return -1

for n in test_list:
    print check(n)
