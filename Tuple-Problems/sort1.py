t = (1,2,3,4,5)
flag = True
for i in range(len(t)-1):
    if t[i] > t[i+1]:
        print('not sorted: ')
        flag = False
        break

if(flag):
    print('Sorted: ')