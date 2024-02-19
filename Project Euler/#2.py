#!/bin/python

import sys
test_list=[]
t = int(raw_input().strip())
for a0 in xrange(t):
    test_list.append(int(raw_input().strip()))
    
def FibSum(x):
    fibs=[1,1]
    while fibs[-1]+fibs[-2]<x:
        fibs.append(fibs[-1]+fibs[-2])
    total=0
    for i in fibs:
        if i%2==0:
            total+=i
    return total
    
            
for i in test_list:
    print FibSum(i)
