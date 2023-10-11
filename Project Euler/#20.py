# Enter your code here. Read input from STDIN. Print output to STDOUT
n=int(raw_input())
test_list=[]
for i in range(n):
    test_list.append(int(raw_input()))

fact_list=[1,1,2]
for i in range(3,1000):
    fact_list.append(i*fact_list[-1])

def digit_sum(n):
    total=0
    string_n=str(fact_list[n])
    for i in range(len(string_n)):
        total+=int(string_n[i])
    return total

for i in test_list:
    print digit_sum(i)
