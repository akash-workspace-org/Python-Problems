L1 = [1,3,4,5]
L2 = [5,9,1,7]
result = []
for i in L1:
    for j in L2:
        if i == j:
            result.append(j)

print(result)