data = open("input.txt", "r").read()

l = list(map(int, data.split('\n')[:-1]))
ans = 0
for i in l:
    while i > 0:
        ans += i//3 - 2
        i = i//3 - 2
    ans -= i
print(ans)

