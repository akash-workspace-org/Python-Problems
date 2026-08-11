L1 = [1,2,3,4,5,6,7,8,9]
even = []
odd = []
key1 = 'Even'
key2 = 'Odd'
dic = {}
for i in L1:
    if i %2 == 0:
        even.append(i)
    else:
        odd.append(i)

dic[key1] = even
dic[key2] = odd



print(dic)








#{
#    'even': [2, 4, 6],
#    'odd': [1, 3, 5]
#}