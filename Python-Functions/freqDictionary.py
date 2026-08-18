def Frequency(x):
    """ This code takes a list and return a dictionary containing the frequency of every element
    """
    printed = []
    dic = {}
    for i in x:
        if i not in printed:
            count = 0
            for j in x:
                if i == j:
                    count+=1
            dic[i] = count
            printed.append(i)
    return dic
print(Frequency([1,1,1,2,3,4,1]))