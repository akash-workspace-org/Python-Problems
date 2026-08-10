s = input('Enter the string: ')
word = list(s.split())
empty = {}
for i in word:
    if i not in empty:
        count = 0

        for j in word:
            if i == j:
                count+=1

        empty[i] = count

print(empty)