'''
print m to n < user input, use recursion
'''

def printing(m,n):
    if m == n:
        print(m) # I have used this to make it look good at terminal, :)
        return 
    print(f"{m}-->",end="")
    printing(m+1,n) 

# recursion tail case
def backprint(m,n):
    if m == n:
        print(m,end="")    # 1 2 3 4 5 6 7 8 9
    else:
        backprint(m+1,n)
        print(f"<--{m}",end="")

# recursion head case  
def head_backprint(m,n):
    if n == m:
        print(m,end="")
        return
    else:
        print(f"{n}--",end="") 
        head_backprint(m,n-1) 

def summation(m,n,sum):
    if m == n:
        print(sum) 
        return 
    sum = sum + m
    summation(m+1,n,sum)




m,n = [int(x) for x in input("2 number and space,ex: 1 10 :>").split(" ")] 
while True:
    x= "1: Iteration from m to n\n2:Reverse Print n to m using tail\n3:Reverse print using n to m using head\n4:Print summation"
    print(x)
    option = int(input("choose between 1 to 4: "))
    print()
    if option == 1:
        printing(m,n)
  
    elif option == 2:
        backprint(m,n) 
        print()
    elif option == 3:
        head_backprint(m,n) 
        print()
    elif option == 4:

        summation(m,n,0)
        print()
    else:
        print("Exit....")
        break

