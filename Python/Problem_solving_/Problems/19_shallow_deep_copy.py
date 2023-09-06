import copy

original_list = [1,2,3,4,5]
shallow_copy = copy.copy(original_list)
deepcopy = copy.deepcopy(original_list)
original_list[1] = 45

print(shallow_copy)
print(original_list)


deepcopy = copy.deepcopy(original_list)
print(original_list)