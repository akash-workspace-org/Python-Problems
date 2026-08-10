d1 = {'a':1,'b':2,'c':3}
d2 = {'d':4,'e':5,'f':6}
d3 = {}
for i in d1:
    d3[i] = d1[i]
    for j in d2:
        d3[j] = d2[j]