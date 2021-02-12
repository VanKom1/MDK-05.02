class Tesseract():
    def __init__(self, a):
        self.a = a
    def s(self):
        return (self.a ** 4)


class Pyramid():
    S = 0
    h = 0
    def __init__(self,S,h):
        self.h = h
        self.S = S

    def s(self):
        return ((1 / 3) * self.S * self.h)


class Sphere():
    r = 0
    def __init__(self,r):
        self.r = r

    def s(self):
        return ((4 / 3 )* 3.14 * self.r ** 3)


a = Tesseract(5)
b = Pyramid(10,3)
c = Sphere(5)

lst = [a, b, c]
for i in lst:
    print(i.s())
