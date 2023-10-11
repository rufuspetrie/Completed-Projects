# Enter your code here. Read input from STDIN. Print output to STDOUT
n=int(raw_input())
test_list=[]
for i in range(n):
    test_list.append(int(raw_input()))
    
def digit_sum(n):
    power=2**n
    total=0
    power_string=str(power)
    for i in range(len(power_string)):
        total+=int(power_string[i])
    return total

for i in test_list:
    print digit_sum(i)
