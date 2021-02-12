S = 0
sp = 0
class Road:
    S = 0
    sp = 0
    def __init__(self,S,sp):
        self.sp = input("Скорость машины ")
        self.S = input("Растояние ")
    def time(self):
        a1 = self.S
        b1 = self.sp
        a1 = int(a1)
        b1 = int(b1)
        d = a1 / b1
        print("Что бы проехать ",self.S," со скоростью " + self.sp + " нужно",d,"час(а)")
Fun = Road(S,sp)
Fun.time()
        