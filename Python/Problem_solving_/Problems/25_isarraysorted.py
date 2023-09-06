def sorting_check(l):
    new_sorted = sorted(l)
    rev_sorted = sorted(l,reverse=True)
    if l == new_sorted or l == rev_sorted:
        return True
    else:
        return False


print(sorting_check([1,2,3,4,5]))
print(sorting_check([2,3,4,1,2,323]))





