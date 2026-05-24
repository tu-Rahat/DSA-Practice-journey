
def ascending(arr):
    l = len(arr)
    for i in range(1,l):
        if arr[i]<arr[i-1]:
            key = arr[i]
            j = i - 1
            while j>=0 and arr[j]>key:
                arr[j+1] = arr[j]
                j  = j - 1
            arr[j+1] = key 

# 1 2 3 4

def descending(arr):
    l = len(arr)
    for i in range(1,l):
        if arr[i]>arr[i-1]:
            key = arr[i] 
            j = i - 1
            while j>=0 and arr[j]<key:
                if arr[j]<key:
                    arr[j+1] = arr[j]
                    j = j - 1
                arr[j+1] = key 

arr= [1,2,3,4,4,4,4,5]
descending(arr)
print(arr)
