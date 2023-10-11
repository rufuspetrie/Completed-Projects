# Enter your code here. Read input from STDIN. Print output to STDOUT
import math
n=int(raw_input())
lower=10**(n-1)+1
upper=10**n
start=int(math.ceil(lower**(1.0/n)))
while start**n<upper:
    print start**n
    start+=1
