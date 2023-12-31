#!/bin/python
# Ideas for improvement:
# Sieve of Eratosthenes
# Sum array

import math
import sys

test_list=[]
t = int(raw_input().strip())
for a0 in xrange(t):
    n = int(raw_input().strip())
    test_list.append(n)

def atkin(nmax):
    is_prime = dict([(i, False) for i in range(5, nmax+1)])
    for x in range(1, int(math.sqrt(nmax))+1):
        for y in range(1, int(math.sqrt(nmax))+1):
            n = 4*x**2 + y**2
            if (n <= nmax) and ((n % 12 == 1) or (n % 12 == 5)):
                is_prime[n] = not is_prime[n]
            n = 3*x**2 + y**2
            if (n <= nmax) and (n % 12 == 7):
                is_prime[n] = not is_prime[n]
            n = 3*x**2 - y**2
            if (x > y) and (n <= nmax) and (n % 12 == 11):
                is_prime[n] = not is_prime[n]
    for n in range(5, int(math.sqrt(nmax))+1):
        if is_prime[n]:
            ik = 1
            while (ik * n**2 <= nmax):
                is_prime[ik * n**2] = False
                ik += 1
    primes = []
    for i in range(nmax + 1):
        if i in [0, 1, 4]: pass
        elif i in [2,3] or is_prime[i]: primes.append(i)
        else: pass
    return primes

# create array that holds sum of primes less than index
x=set(atkin(1000000))
bool_array=[False]*1000000
for i in range(len(bool_array)):
    if i in x:
        bool_array[i]=True

sum_array=[0]*1000000
y=0
for i in range(len(sum_array)):
    if bool_array[i]:
        y+=i
    sum_array[i]=y

for i in test_list:
    print sum_array[i]
