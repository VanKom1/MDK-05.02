a = 0
b = 0
class File:
    a = 0
    b = 0
    def __init__(self,a,b):
        self.a = input("Сколько всего файлов ")
        self.b = input("Сколько файлов удалили ")
    def out(self):
        a1 = self.a
        b1 = self.b
        a1 = int(a1)
        b1 = int(b1)
        d = a1 - b1
        print("После удаления " + self.b + " файлов из " + self.a + " осталось ",d)
Fun = File(a, b)
Fun.out()