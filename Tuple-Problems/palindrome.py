t = ('m','a','d','a','m')
flag = True
for i in range(0,len(t)//2):
    if t[i] != t[len(t)-i-1]:
        flag = False
        print('not palindrome: ')
        break

if(flag):
    print('Palindrome: ')