d = {'a':1,'b':2,'c':3}
empty = {}
for i in d:
    empty[d[i]] = i # Ek eye line mein key ko value se swap kr rahi he

print(empty)