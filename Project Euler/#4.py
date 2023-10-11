#!/bin/python
# note: 6 digit palindromes are divisible by 11
import sys

test_list=[]
t = int(raw_input().strip())
for a0 in xrange(t):
    n = int(raw_input().strip())
    test_list.append(n)
    
def largest_palindrome(n):
    largest=0
    for i in range(100,1000):
        for j in range(110,1000,11):
            temp=str(i*j)
            temp_s=temp[::-1]
            if temp==temp_s and int(temp)<n and int(temp)>largest:
                largest=int(temp)
    return largest

for i in test_list:
    print largest_palindrome(i)
