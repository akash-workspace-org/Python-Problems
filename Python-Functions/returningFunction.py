def func_1():
    """ This is a nested function example
    """
    a = 5
    print(a**2)
    def func_2():
        b = 3
        if b%2==0:
            print('Even: ')
        else:
            print('Odd: ')
        def func_3():
            z,x = (2,5)
            if z > x:
                print('z is greater: ')
            else:
                print('x is greater: ')
            def func_4(a,b):
                return a+b
            return func_4
        return func_3
    return func_2
z = func_1()()()(2,4)
print(z)