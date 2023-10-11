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

def primes(n):
    
    if n<=prime_list[-1]:
        return prime_list[n-1]
    k=prime_list[-1]+2
    while prime_list[-1]<n:
        if isPrime(k,prime_list):
            prime_list.append(k)
        k+=2
    return prime_list

x=primes(max(test_list))
for i in test_list:
    primes=[y for y in x if y<=i]
    highest=[1]*len(primes)
    for j in range(len(highest)):
        while highest[j]*primes[j]<=i:
            highest[j]*=primes[j]
    total=1
    for i in highest:
        total*=i
    print total
'''
Pro tip: M is divisible by all numbers from 1 to N iff M is equal to the product of all prime powers p^k where p is prime and divides M, and p < N, and k is the largest integer such that p^k < N. For example, 2520 = 2^3 * 3^2 * 5 * 7.
'''
