# Первое задание
a = 5
b = 10
a = a + b 
b = a - b 
a = a - b 
print(a,b)
a = 5
b = 10
a, b = b, a
print(a,b)
# Второе задание
a = input()
k = 0
for i in range(0,len(a)):
    b = int(a[i])
    k += b
print(k)
#Третье задание
#ax2+bx+c=0
import math
a, b, c = map(int, input().split())

d = b * b - 4 * a * c
if d > 0:
    x1 = (-b + math.sqrt(d)) / (2 * a)
    x2 = (-b - math.sqrt(d)) / (2 * a)
    print(x1,x2)
elif d == 0:
    x = -b / (2 * a)
    print(x)
else:
    print("нет решений(они есть, но там комплексные числа и все такое)")
