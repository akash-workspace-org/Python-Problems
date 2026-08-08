s1 = {1,2,3,4,5}
s2 = {1,3,4,8,9}
result = set()
for i in s1:
    if i not in s2: 
        result.add(i)

print(result)

# phele set ke wo element jo dosre set mein nai honge wo result mein store hojai ge