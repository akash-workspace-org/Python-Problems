def total(x):
    """ This calculate sum of numbers in list
    """
    list_sum = 0
    for i in x:
        list_sum = list_sum + i
    return list_sum
print(total([1,2,3,4,5]))