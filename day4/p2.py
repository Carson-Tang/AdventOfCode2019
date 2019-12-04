ans = 0

def check(v):
    s = str(v)
    flag = False
    for i in range(0,5):
        if s[i] > s[i+1]:
            return False
        if s[i] == s[i+1]:
            if i != 0 and s[i] == s[i-1]:
                continue
            if i < 4 and s[i] == s[i+2]:
                continue
            flag = True
    return flag

for i in range(372304, 847061):
    if check(i):
        print(i)
        ans+=1
print(ans)

