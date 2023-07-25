def maximum(arr):
    m=arr[0]
    for i in range(0,len(arr)):
        if arr[i]>m:
            m=arr[i]
    return m