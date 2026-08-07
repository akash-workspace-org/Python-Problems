t = (1,1,1,2,3,4,5,5,5,5) # -> 5 5 5 5 = output will be 4
count = 1
count_max = 1
for i in range(1,len(t)):
    if t[i] == t[i-1]:
        count+=1
    else:
        count = 1
    if count > count_max:
        count_max = count

print(count_max)

# Ye wo element count krega jo countinously use hoa ho.