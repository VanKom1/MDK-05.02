i = 0
a, b = map(int, input().split())
a1 = 0
b1 = 0
st = 1
r = 0
while i == 0:
    comand = input()
    if comand == "вперед":
        a1 += st
    elif comand == "направо":
        a1, b1 = b1, a1
        if st == -1:
            st == -st
        r += 1
    elif comand == "налево":
        a1, b1 = b1, a1
        if st ==  1:
            st = -st
        r -= 1
    elif comand == "разворот":
        st = -1
    elif comand == "стоп":
        if r % 2 == 0:
            i += 1
            print("Вы нашли клад,клад находитьсяя на",a1,b1)
        else:
            i += 1
            print("Вы нашли клад,клад находитьсяя на",b1,a1)
    else:
        print("Нет такой команды")
      
