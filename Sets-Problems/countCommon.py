a = {1,2,3,4,5}
b = {3,4,6}
count = 0
for i in a:
    for j in b:
        if i == j:
            count+=1

print(count)