L = [1,2,2,3,4,5]
flag = True
for i in range(len(L)-1):
    if L[i] == L[i+1]:
        flag = False
        print('Dublicate found: ',L[i])
        break

if(flag):
    print('Not found: ')