def remove(x):
    """ This code remove duplicate elements"""
    L = []
    for i in x:
        if i not in L:
            L.append(i)
    return L
print(remove(x=[1,1,2,2,3,4]))