a = {1,2} # Keya a ke elements b mein he
b = {1,2,3,4,5}
flag = True
for i in a:
    if i not in b:
        flag = False
        print('Not subset: ')
        break

if(flag):
    print('Subset: ')