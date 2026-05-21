arr = [1,2,3,4,5] 

# 1 2 3 4 5

def rev(arr,l,r):
    if l>=r:
        return
    rev(arr,l+1,r-1) # head recursion
    arr[l],arr[r] = arr[r],arr[l]
    # rev(arr,l+1,r-1) Tail recursion
rev(arr,0,len(arr)-1)
print(arr)