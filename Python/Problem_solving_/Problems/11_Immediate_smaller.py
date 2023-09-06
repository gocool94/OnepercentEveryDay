def immediateSmaller(arr,n,x):
    closest = -1  # Initialize to None
    for num in arr:
        if num < x and (closest is None or x - num < x - closest):
            closest = num
    return closest

print(immediateSmaller([2,3,4,5],1,-1))