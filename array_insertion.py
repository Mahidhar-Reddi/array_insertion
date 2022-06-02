def common(arr1, arr2):
    arr3 = []
    for i in range(len(arr1)):
        if arr1[i] in arr2:
            print(arr1[i], end = " ")
    
common([1,4,2,5],[7,1,1,2,4])
