def prime(x,y):
    """ This code take start to end number from user then print prime numbers between them 
    """
    L = []
    for i in range(x,y+1):
        flag = True
        for j in range(2,i):
            if i%j == 0:
                flag = False
                break
        if flag:
            L.append(i)
    return L

print(prime(x=2,y=10))