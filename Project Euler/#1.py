#!/bin/python

import sys
test_list=[]
t = int(raw_input().strip())
for a0 in xrange(t):
    test_list.append(int(raw_input().strip()))

def tf(x):
    a=(x-1)/3
    b=(x-1)/5
    c=(x-1)/15
    ax=(a*(a+1))*3
    bx=(b*(b+1))*5
    cx=(c*(c+1))*15
    dx=100*(ax+bx-cx)
    ex=dx/200
    return int(ex)
    
for i in test_list:
    print tf(i)
