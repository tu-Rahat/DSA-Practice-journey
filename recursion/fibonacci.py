'''
a,b = 0,1
sum = 0
# 0 1 1 2 3 5 8 13 21

# 0 a1 a1 a2 b3   
print(f"{a} {b}",end=" ")
for i in range(40-2):
    sum = a + b
    a = b
    b = sum
    print(sum,end=" ")
'''
def fibonacchi(n):
    if n==1:
        return 1
    elif n == 0:
        return 0
    else:
        
        return fibonacchi(n-1) + fibonacchi(n-2)        
print(fibonacchi(5))

'''
    0 1 1 2 3 5
    f(2) = 1 + 0 = 1
    f(3) = f(2) + f(1) = 1 + 1 = 2
    f(4) = f(3) + f(2) = 2 + 1 = 3
    f(5) = f(4) + f(3) = 3 + 2 = 5

'''