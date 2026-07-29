L = [1,10,100,20,400]
largest = L[0]
secLargest = L[0]
for i in L:
    if i > largest:
        largest = i

for j in L:
    if j > secLargest and j != largest:
        secLargest = j
print('Largest number is: ',largest)
print('Second largest numbers is: ',secLargest)