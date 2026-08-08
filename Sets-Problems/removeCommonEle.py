a = {1,2,3,4,5} # This code remove common ele in both of sets
b = {3,4,5,6,7}
result = set()
for i in a:
    if i in b:
        result.add(i)

for i in result:
    a.remove(i)
    b.remove(i)

print('common ',result)
print('a',a)
print('b',b)

# Eys code mein phele hm common ele nikal rahi hein pher result pr loop chala kr a and b ke
# common ele delete kr rahi he
