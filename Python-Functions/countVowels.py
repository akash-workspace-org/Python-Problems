def vowel(x):
    total = 0
    for i in x:
        if i == 'a' or i == 'i' or i == 'u' or i == 'e' or i == 'o':
            total+=1
    return total

print(vowel('akash'))