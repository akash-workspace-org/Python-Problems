t = (20,39,99,70,100)
larg = t[0]
secLarg = t[0]
for i in t:
    if i > larg:
        larg = i
for j in t:
    if j > secLarg and j != larg:
        secLarg = j

print(larg)
print(secLarg)