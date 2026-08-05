n = int(input('Enter the number: '))
t = (1,2,1,2,1,4,6,7)
count = 0
for i in t:
    if i == n:
        count+=1

print(n,'->',count)