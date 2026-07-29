L = [1,1,2,3,5,2]
L1 = []
for i in range(len(L)-1):
    if L[i] != L[i+1]:
        L1.append(i)

print(L1)