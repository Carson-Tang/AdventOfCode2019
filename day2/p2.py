data = open("input.txt", "r").read()


def check(a, b):
    l = list(map(int, data.split(',')))
    l[1] = a
    l[2] = b

    for i in range(0,len(l),4):
        if l[i] == 99: break
        if l[i] == 1:
            l[l[i+3]] = l[l[i+1]] + l[l[i+2]]
        elif l[i] == 2:
            l[l[i+3]] = l[l[i+1]] * l[l[i+2]]

    return l[0] == 19690720

for i in range(0,100):
    for j in range(0, 100):
        if check(i,j):
            print(100*i + j)
            break
