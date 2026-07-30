L1 = [1,3,5]
L2 = [2,4,6]
L3 = []

for i in L1+L2:
    L3.append(i)

    for k in range(len(L3)):
        for x in range(k+1,len(L3)):
            if L3[k] > L3[x]:
                temp = L3[k]
                L3[k] = L3[x]
                L3[x] = temp

print(L3)