# newlist = [expression for item in iterable if condition == True]

new_List = [i for i in range(10) if (i % 2 == 0)]
print(new_List)
newlist = [x if x != 2 else 10 for x in range(10)]
print(newlist)


# result = [expression_if_true if condition else expression_if_false for item in iterable]
