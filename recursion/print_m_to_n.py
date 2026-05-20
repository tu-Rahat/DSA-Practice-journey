'''
print m to n < user input, use recursion
'''

def printing(m,n):
    if m == n:
        print(m) # I have used this to make it look good at terminal, :)
        return 
    print(f"{m}-->",end="")
    printing(m+1,n) 

m,n = [int(x) for x in input().split(" ")] 
printing(m,n)