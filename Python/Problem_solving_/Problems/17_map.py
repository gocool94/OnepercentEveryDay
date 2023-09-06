lst = [10, 2, 14, 25, 17]

square = list(map(lambda x: x ** 2, lst))

print(square)
import pandas as pd

l1 = [1,2,3,4]
l2 = [2,3,4,5]

m3 = pd.DataFrame((zip(l1,l2)))

print(m3)

def multipleby2(num):
    return num * 2

new_list = list(map(multipleby2,l1))
print(new_list)