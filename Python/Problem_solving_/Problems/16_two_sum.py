"""
Given an array of integers nums and an integer target,
return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution,
and you may not use the same element twice.

You can return the answer in any order.


"""

def twoSum(nums, target):
    for i in range(0,len(nums)):
        for j in range(i,len(nums)):
            print(i,j)

print(twoSum([2,7,11,15],9))
print("***********************************")
print(twoSum([3,2,4],6))
print("***********************************")
print(twoSum([3,3],6))
print("***********************************")

"""
i[0] -> i[1] i[2] i[3] i[4]
i[1] -> i[0] i[2] i[3] i[4] 
i[2] -> i[0] i[1] i[3] i[4]
i[3] -> i[0] i[1] i[2] i[4]
i[4] -> i[0] i[1] i[2] i[3]






"""


#TODO: Learn enumerate
# complete this problem
# understand the concepts here
