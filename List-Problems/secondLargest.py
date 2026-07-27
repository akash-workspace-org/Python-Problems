L = [1,10,20,4]
largest = L[0]
secLargest = L[0]
for i in L:
    if i > largest:
        largest = i
        for i in L:
            if i > largest and i != largest:
                secLargest = largest
print('Largest number is: ',largest)
print('Second largest numbers is: ',secLargest)