#!/bin/python

import sys
test_list=[]
t = int(raw_input().strip())
for a0 in xrange(t):
    n,k = map(int,raw_input().strip().split(' '))
    #n,k = [int(n),int(k)]
    num = int(raw_input().strip())
    test_list.append([k,num])
    
def series_product(n):
    k=n[0]
    num=str(n[1])
    length=len(num)
    product_list=[]
    num_list=[]
    for i in range(0,length):
        num_list.append(int(num[i]))
    i=0
    while i+k<=length:
        list=num_list[i:i+k]
        product=1
        for n in list:
            product*=n
        product_list.append(product)
        i+=1
    max=-1000000
    for i in product_list:
        if i>max:
            max=i            
    return max

for i in test_list:
    print series_product(i)
