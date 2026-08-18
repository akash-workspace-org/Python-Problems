def secMax(x):
    large = x[0]
    second = x[0]
    for i in x:
        if i > large:
            large = i
    for j in x:
        if j > second and j != large:
            second = j
    return second
print(secMax([1,2,3,4,5]))