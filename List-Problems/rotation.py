L = [1,2,3,4,5]
last = L[-1]
for i in range(len(L)-1,0,-1):
    L[i] = L[i-1]

L[0] = last
print(L)