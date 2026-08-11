d = {'a':22,'b':22,'f':44,'g':21}
result = {}
for i in d:
    if d[i] not in result.values():
        result[i] = d[i]

print(result)