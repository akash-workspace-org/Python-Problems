def reverseList(x):
    L = []
    for i in range(len(x),0,-1):
        L.append(i)
    return L
print(reverseList([1,2,3,4,5,6]))