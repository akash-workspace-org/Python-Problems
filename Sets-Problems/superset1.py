a = {1,2,3,4} # Keya b ke element a mein he
b = {2,4}
flag = True
for i in b:
    if i not in a:
        flag = False
        print('Not superset: ')

if(flag):
    print("Superset: ")