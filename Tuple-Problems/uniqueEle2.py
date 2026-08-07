t = (1,1,2,3,4,4,5)
for i in t:
    count = 0
    for j in range(len(t)):
        if t[j] == i:
            count+=1
    if count == 1:
        print(i,end=" ")

# wo elements print honge jo sirf ek baar use hoye he