x = str(input())
k = 0
lst = list(x)
print(lst[2])
print(lst[-2])
for i in range(0,5):
    print(lst[i],end = '')
print()
for i in range(0,len(lst) - 2):
    print(lst[i],end = '')
print()
for i in range(0,len(lst),2):
    print(lst[i],end = '')
print()
for i in range(1,len(lst),2):
    print(lst[i],end = '')
print()
lst.reverse()
for i in range(0,len(lst),):
    print(lst[i],end = '')
print()
for i in range(0,len(lst),2):
    print(lst[i],end = '')
print()
for i in range(0,len(lst)):
    k += 1
print(k)
