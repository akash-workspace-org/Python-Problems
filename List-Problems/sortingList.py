L = list(input('Enter the number: '))
for i in range(len(L)):
    for j in range(i+1,len(L)):
        if L[i] > L[j]:
            temp = L[i]
            L[i] = L[j]
            L[j] = temp

print(L)