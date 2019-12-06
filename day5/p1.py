data = open("input.txt", "r").read()

l = list(map(int, data.split(',')))

def add(pos,a,b):
    l[pos] = a+b
def mul(pos,a,b):
    l[pos] = a * b
def three(pos):
    l[pos] = int(input())
def four(pos):
    print(l[pos])

i = 0
while True:
    s = "0000"+str(l[i])
    cmd = int(s[-2:])
    p1 = int(s[-3])
    p2 = int(s[-4])
    if cmd == 99: break
    if cmd == 3:
        three(l[i+1])
    if cmd == 4:
        four(l[i+1])
    if cmd == 3 or cmd == 4:
        i += 2
        continue
    a = l[l[i+1]] if p1 == 0 else l[i+1]
    b = l[l[i+2]] if p2 == 0 else l[i+2]
    pos = l[i+3]
    if cmd == 1:
        add(pos,a,b)
    if cmd == 2:
        mul(pos,a,b)
    i += 4

