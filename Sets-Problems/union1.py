t1 = {1,2,3,4}
t2 = {1,2,5,6}
result = set()
for i in t1:
    result.add(i)
    for j in t2:
        result.add(j)

print(result)

# Set duplicate element ko autometicaly remove kr deta hein