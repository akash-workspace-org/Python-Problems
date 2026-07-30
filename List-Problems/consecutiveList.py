L = [1,1,2,1,2,2,1,1,1,2]
count = 1
max_count = 1

for i in range(1,len(L)):
    if L[i] == L[i-1]:
        count+=1
    else:
        count = 1
    if count > max_count:
        max_count = count

print(max_count)

# Jo same elements ek sequense me sab se zada use hoa he wahi count ho rah he
# ex
# 1 lagatar ek sequense mein 3 bar use hoa he eys lye wahi count hoga