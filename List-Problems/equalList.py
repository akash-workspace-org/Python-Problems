L1 = [1,2,3]
L2 = [1,2,3]
flag = True
for i in range(len(L1)):
    if L1[i] != L2[i]:
        flag = False
        print("list are not equal: ")
        break

if(flag):
    print('List are equal: ')