L = [1,1,1,2,3,1,2]
printed = []
for i in L:
        if i not in printed:
            count = 0
            for j in L:
                if i == j:
                    count+=1
            print(i,'->',count)
            printed.append(i)