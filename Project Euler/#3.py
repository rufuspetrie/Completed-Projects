import sys, math
testList=[]

t = int(raw_input().strip())
for a0 in xrange(t):
    n = long(raw_input().strip())
    testList.append(n)

def largest_prime_factor(n):
    x=2
    while x**2<=n:
        if n%x==0:
            n/=x
        else:
            if x>2:
                x+=2
            else:
                x+=1
    return n

for i in testList:
    print largest_prime_factor(i)
