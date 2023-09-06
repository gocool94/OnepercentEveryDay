l = [1,2,3,4,5,23,21]

def second_largest(l):
    if(len(l)<=1):
        return None
    larg = l[0]
    slarg = None
    for i in l[1:]:
        if (i > larg):
            slarg = larg
            larg = i
        elif(i!=larg):
            if (slarg == None or slarg < i):
                slarg = i
    return slarg

print(second_largest(l))