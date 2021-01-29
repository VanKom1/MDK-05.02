d = int(input())
m = int(input())
t = 0
m = m -2
if m == 1:
    m = 11
    t = 1
if m == 2:
    m = 12
    t = 1
a = int(input()) + t
y = a % 100
c = a // 100
print((d + ((13*m - 1) // 5 ) + y + (y //4 + c // 4 - 2*c + 777))%7)
