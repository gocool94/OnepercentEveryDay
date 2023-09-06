def deleteFromArray(arr,n,idx):
    #code here
    del arr[idx]
    print(arr)
    arr.append(0)

    print(arr)
    return arr

deleteFromArray([1,2,3,4,5],5,0)