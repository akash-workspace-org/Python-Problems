n = int(input("Enter the number: "))
t = (1,2,3,1,2)
count = 0
for i in t:
    if n == i:
        count+=1

print(count)