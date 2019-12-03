data = open("input.txt", "r").read()

l = list(map(int, data.split('\n')[:-1]))
ans = 0
for i in l: ans += i//3 - 2
print(ans)
