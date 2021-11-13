import sys,time
class giao():
    def bianyi(self,m):
        if 'cin' in m:
            a = str(m[3:5])
            b = int(m[5:len(m)])
            self.a = a
            self.b = b
        if 'go' in m:
            if 'go' == m:
                print('ero')
            elif ' ' not in m:
                print('ero')
            elif '-n' in m:
                print(self.x)
            else:
                print(m[3:len(m)])
        if 'inpot' in m:
            x = input(m[5:len(m)])
            self.x = x
    def pio(self,m):
        for i in m:
            sys.stdout.write(i)
            sys.stdout.flush()
            time.sleep(0.05)

import sys,time
main = '-->'
xp = []
n = giao()
while True:
    c = input(main)
    xp.append(c)
    if 'os' == c:
        for i in range(len(xp)):
            n.bianyi(xp[i])
        xp = []
    if 'help' == c:
        print('1.go 输出如go ji 2.inpot 输入如inpotname（结果使用go -n输出） 3.os运行 4.cin 变量如cinoi12，go oi，os 结果12 5.pch用于更改提示语如改前-->，使用pchoi，变成oi')
    if 'pch' in c:
        main = c[3:len(c)]
    if 'zou' == c:
        break

n.pio('记得点小心心')