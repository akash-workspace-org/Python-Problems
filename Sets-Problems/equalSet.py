a = {1, 4}
b = {1, 2, 3}

flag = True

if len(a) != len(b):
    flag = False
else:
    for i in a:
        if i not in b:
            flag = False
            break

if flag:
    print("Equal")
else:
    print("Not Equal")