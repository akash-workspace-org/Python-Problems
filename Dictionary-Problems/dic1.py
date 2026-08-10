student = {'aa':33,'bb':22,'cc':217}
maximum = 22
max_key = 'age'
for i in student:
    if student[i] < maximum:
        maximum = student[i]
        max_key = i


print(max_key,maximum)