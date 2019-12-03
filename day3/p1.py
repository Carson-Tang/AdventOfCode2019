data = open("input.txt", "r").read()


l = data.split('\n')
c1 = l[0].split(',')
c2 = l[1].split(',')
ans = 99999999
d = {}

def run(c, flag):
    global ans
    x = 0
    y = 0
    for i in range(len(c)):
        cmd = c[i][0]
        s = int(c[i][1:])
        for j in range(s):
            if cmd == 'R': x+=1
            elif cmd == 'D': y-=1
            elif cmd == 'U': y+=1
            elif cmd == 'L': x-=1
            if flag and (x,y) in d:
                ans = min(ans, abs(x)+abs(y))
            if not flag: d[(x,y)] = 1


run(c1,0)
run(c2,1)
print(ans)
