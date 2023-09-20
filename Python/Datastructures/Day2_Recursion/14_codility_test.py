"""
Write a function:

def solution(A)

that, given an array A of N integers, returns the smallest positive integer (greater than 0) that does not occur in A.

For example,

Given A = [1, 3, 6, 4, 1, 2], the function should return 5.

Given A = [1, 2, 3], the function should return 4.

Given A = [−1, −3], the function should return 1.

"""


def solution(A):
    count = {}  # Dictionary to store counts of each value
    max_x = 0  # Initialize the maximum value of x
    # Count the occurrences of each value in the array
    for num in A:
        if num in count:
            count[num] += 1
        else:
            count[num] = 1

    # Iterate through the dictionary to find the biggest x
    print(count)
    for num, x in count.items():
        print(f"the number is {num} and the x value is {x}")
        if num == x:
            max_x = max(max_x, x)
    #       print(max_x)

    return max_x

max_value = max(1,2,3,4,8)
print(max_value)


# Test cases
print(solution([3, 1, 4, 1, 5]))  # Output: 2 (value 3 occurs twice)

