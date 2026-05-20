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

m,n = [int(x) for x in input("2 number and space,ex: 1 10 :>").split(" ")] 
while True:
    option = int(input("choose between 1 to 3: "))
    print()
    if option == 1:
        printing(m,n)
  
    elif option == 2:
        backprint(m,n) 
        print()
    elif option == 3:
        head_backprint(m,n) 
        print()
    else:
        print("Exit....")
        break

