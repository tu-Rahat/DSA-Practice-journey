'''
print m to n < user input, use recursion
'''

def printing(m,n):
    if m == n:
        print(m) # I have used this to make it look good at terminal, :)
        return 
    print(f"{m}-->",end="")
    printing(m+1,n) 


def backprint(m,n):
    if m == n:
        print(m,end="")    # 1 2 3 4 5 6 7 8 9
    else:
        backprint(m+1,n)
        print(f"<--{m}",end="")


m,n = [int(x) for x in input().split(" ")] 
printing(m,n)

print("-------<<---------->>-------------")
print("Reverse print") 

backprint(m,n) 


