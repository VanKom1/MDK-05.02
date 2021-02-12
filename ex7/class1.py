id = 0
name = 0
age = 0
class User:
    id = 0
    name = 0
    age = 0
    def __init__(self,id,name,age):
        self.id = input("id ")
        self.name = input("Имя пользователя ")
        self.age = input("Возраст ")
    def out(self):
        print(self.id,self.name,self.age)
Fun = User(id, name, age)
Fun.out()