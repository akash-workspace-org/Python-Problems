L = list(input('Enter the number: '))
for i in L:
    count = 0
    for j in range(len(L)):
        if L[j] == i:
            count+=1
    if count == 1:
        print(i,end=" ")