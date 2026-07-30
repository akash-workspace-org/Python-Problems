L = list(input('Enter the number: '))
printed = []
for i in L:
    if i not in printed:
        count = 0
        for j in L:
            if i == j:
                count+=1
        print(i,'->',count)
        printed.append(i)

#Ye code har ek unique element ko count kr rah he, aur print kr rah he 