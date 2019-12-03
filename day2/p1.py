data = open("input.txt", "r").read()

l = list(map(int, data.split(',')))
l[1] = 12
l[2] = 2

for i in range(0,len(l),4):
    if l[i] == 99: break
    if l[i] == 1:
        l[l[i+3]] = l[l[i+1]] + l[l[i+2]]
    elif l[i] == 2:
        l[l[i+3]] = l[l[i+1]] * l[l[i+2]]

print(l)
print(l[0])
