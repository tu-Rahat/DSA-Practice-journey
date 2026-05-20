m,n = 0,10

def summation(m,n):
    if m == n:
        return m
    return m + summation(m+1,n)

print(summation(m,n))

     