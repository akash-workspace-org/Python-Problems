d = {'a':33,'b':66,'c':77,'y':12}
mx = 33
key = 'a'
sMx = 66
sKey = 'b'
for i in d:
    if d[i] > mx:
        mx = d[i]
        key = i
for j in d:
    if d[j] > sMx and d[j] != mx:
        sMx = d[j]
        sKey = j

print(mx)
print(sMx)