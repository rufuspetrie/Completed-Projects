#!/bin/python
# square of sum minus sum of squares

import sys

test_list=[]
t = int(raw_input().strip())
for a0 in xrange(t):
    n = int(raw_input().strip())
    test_list.append(n)
    
def sum_of_squares(n):
    return (n*(n+1)*(2*n+1))/6

def square_of_sum(n):
    sum=(n*(n+1))/2
    return sum**2

for n in test_list:
    print square_of_sum(n)-sum_of_squares(n)
