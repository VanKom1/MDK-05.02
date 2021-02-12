class Class:
   __a = 0
   def geta(self):
       return self.__a
   def seta(self):
       self.__a = input()
       return self.__a
class1 = Class()
print(class1.geta())
class1.seta()
print(class1.geta())

