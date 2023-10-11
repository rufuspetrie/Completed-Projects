# Enter your code here. Read input from STDIN. Print output to STDOUT
n=int(raw_input())
number_list=[]
for i in range(n):
    number_list.append(int(raw_input()))
x=str(sum(number_list))
print x[:10]
