def palindrome(s):
    """ This code check string is palindrome or not
    """
    a = len(s)
    flag = True
    for i in range(0,a//2):
        if s[i] != s[(a)-i-1]:
            flag = False
            return 'Not palindrome'
    if flag:
        return 'Palindrome'

print(palindrome(['madam']))