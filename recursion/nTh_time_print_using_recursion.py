def func(n):
    if n == -1:
         return 
    print("Hello, World!")
    func(n-1) 

n = int(input("Enter a number: "))
func(n) 