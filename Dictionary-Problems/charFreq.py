s = input('Enter the string: ')
empty = {}
for i in s:
    if i not in empty:
        count = 0

        for j in s:
            if i == j:
                count+=1
                
        empty[i] = count

print(empty)
