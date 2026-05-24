arr = [1,2,3,4,5,6,7,8,9]

for i in range(len(arr)):
    maxx = i 
    if i+1<len(arr):
        for j in range(i+1,len(arr)):
            if arr[j] > arr[maxx]:
                maxx = j 
        arr[i],arr[maxx] = arr[maxx],arr[i]
    
print(arr)

'''
O(n) = n**2
'''
