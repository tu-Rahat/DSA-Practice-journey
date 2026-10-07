# https://codeforces.com/group/MWSDmqGsZm/contest/219158/problem/K

inp = [int(x) for x in input().split(" ")] 

min_val = inp[0] 
max_val = inp[0] 

for i in range(len(inp)):
    if min_val >= inp[i]:
        min_val = inp[i] 
    if max_val <= inp[i]:
        max_val = inp[i] 

print(min_val, max_val) 
