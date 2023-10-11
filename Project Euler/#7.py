#!/bin/python

import sys

test_list=[]
t = int(raw_input().strip())
for a0 in xrange(t):
    n = int(raw_input().strip())
    test_list.append(n)
    
def isPrime(n,prime_list):
    for i in prime_list:
        if n%i==0:
            return False
    return True

prime_list=[2,3]

def nth_prime(n):
    
    if n<=len(prime_list):
        return prime_list[n-1]
    
    k=prime_list[-1]+2
    while len(prime_list)<n:
        if isPrime(k,prime_list):
            prime_list.append(k)
        k+=2
    return prime_list[-1]      

for i in test_list:
    print nth_prime(i)
