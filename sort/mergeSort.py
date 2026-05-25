def dnc(arr):
    if len(arr)==1:
        return arr
    
    midd = len(arr)//2
    lar = arr[:midd]
    rar = arr[midd:]
    left_arr = dnc(lar)
    right_arr = dnc(rar) 

    l = len(left_arr)
    r = len(right_arr) 
    i,j,k = 0
    result = []
    while i<l and j<r:
        if left_arr[i]<=right_arr[j]:
            result[k] = left_arr[i]
            i = i + 1
            k = k + 1
        else: 
            result[k] = right_arr[j]
            j = j + 1
            k = k + 1
    while i>=l and j<r:
        result[k] = right_arr[j]
        j = j + 1
        k = k + 1
    while i<l and j >=r:
        result[k] = left_arr[i]
        i = i + 1
        k = k + 1
    return result

arr = [5,4,3,2,1]
dnc(arr) 
print(arr)