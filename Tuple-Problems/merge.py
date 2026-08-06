t1 = (1,2,3,4,5)
t2 = (6,7,8,9)
t3 = (t1+t2)

for j in range(1,len(t3)):
    for k in range(j+1,len(t3)):
        if t3[j] > t3[k]:
            temp = t3[j]
            t3[j] = t3[k]
            t3[k] = temp

print(t3,end=" ")