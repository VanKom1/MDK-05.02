class grass():
    quantity = 10
    satiety = 20
class animal(grass):
    hunger = 100
    def eat(self):
        grass.quantity -= 1
        self.hunger += self.satiety
        return self.quantity , self.hunger
animal = animal()
while True:
    if animal.hunger <= 70 and grass.quantity != 0:
       animal.eat() 
    if  animal.hunger == 0:
        print("Корова умерла от голода")
        break
    animal.hunger -= 10
    print("Уровень сытости коровы равен",animal.hunger)
    print("Количество осташейся травы равен",grass.quantity)
    