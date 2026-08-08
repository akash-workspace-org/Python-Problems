s = {1,2,3,4,5}
s1 = {1,3,4,6,6}
result = set()
for i in s:
    for j in s1:
        if i == j:
            result.add(j)

print(result)