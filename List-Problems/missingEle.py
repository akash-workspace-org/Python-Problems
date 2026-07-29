L = list(input('Enter the numbers: ')) # Missing element are finding
large = L[0]
for i in L:
    if i > large:
        large = i

total = int(large)
result = total*(total+1)//2
actual_sum = 0
for i in L:
    actual_sum = actual_sum+int(i)

final = result - actual_sum

print(result)
print(actual_sum)
print(final)