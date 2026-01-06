class Hero:
    def __init__(self, name):
        self.name = name
        self.level = 1
        self.lives = 3
    def hello(self):
        print('hello')
hero1 = Hero('Frisk')
hero2 = Hero('Chara')
hero1.hello()

class Car:
    def __init__(self, mark, model):
        self.mark = mark
        self.model = model
        self.year = 2020
    def atributes(self):
        print(f'{self.mark, self.model, self.year}')
car1 = Car('Toyota','Camry')
car1.atributes()