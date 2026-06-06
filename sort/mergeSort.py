def dnc(arr):
    if len(arr)==1 or len(arr) ==0:
        return arr
    
    midd = len(arr)//2
    lar = arr[:midd]
    rar = arr[midd:]
    left_arr = dnc(lar)
    right_arr = dnc(rar) 

    l = len(left_arr)
    r = len(right_arr) 
    i,j = 0,0
    result = []
    while i<l and j<r:
        if left_arr[i]<=right_arr[j]:
            result.append(left_arr[i])
            i = i + 1
        
        else: 
            result.append(right_arr[j]) 
            j = j + 1
    print(f"left{left_arr}--Right{right_arr}--result{result}")

    while i>=l and j<r:
        result.append(right_arr[j])
        j = j + 1
    print(f"left{left_arr}--Right{right_arr}--result{result}")
        
    while i<l and j >=r:
        result.append(left_arr[i]) 
        i = i + 1
    print(f"left{left_arr}--Right{right_arr}--result{result}")  # Just for debugging
    return result

arr = [4,3,3,2,1,0]
arr = dnc(arr) 
print(arr)

'''
O(t) = NlogN
O(space) = N , It creates new list 
'''