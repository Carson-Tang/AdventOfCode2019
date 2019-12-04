ans = 0

def check(v):
    s = str(v)
    flag = False
    for i in range(5):
        if s[i] > s[i+1]:
            return False
        if s[i] == s[i+1]:
            flag = True
    return flag

for i in range(372304, 847061):
    if check(i):
        ans+=1
print(ans)
