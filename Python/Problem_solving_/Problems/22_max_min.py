def maximumElement(arr):
    max = 0
    for i in arr:

        if i>max:
            max = i
    return max



def minimumElement(arr):
    min = arr[0]
    for i in arr:
        if i <= min:
            min = i
    return min

print(maximumElement([1,2,3,4,5]))
print(minimumElement([2,3,4,5,5]))
