"""Given an unsorted array arr[] of size N containing non-negative integers.
You will also be given an integer X, the task is to count the number of elements which are strictly greater than X. The given integer may or not be present in the array given.

Example 1:

Input:
N = 5
arr[] = {4 5 3 1 2}
X = 3
Output: 2
Explanation: Here X is 3. The elements
greater than X are 4 and 5."""


def greaterThanX(self,arr,n,x):
    count = 0
    for i in arr:
        if(i>x):
            count+=1
    return count
