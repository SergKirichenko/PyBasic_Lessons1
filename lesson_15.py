# наследование
# инкапсуляция
# декораторы
# модуль requests

def hello():
    return "Hello!"


class Unit:
    def __init__(self, name, health):
        self.name = name
        self.health = health

    def __str__(self):
        return f"{self.name} - H:{self.health}"

    def cure(self):
        self.health += 10

    def say(self):
        return hello()

    # @staticmethod
    # def hello():
    #     return "Hello!"


class Mage(Unit):
    def __init__(self, name, health, ability):
        super().__init__(name, health)
        self.ability = ability

    def __str__(self):
        base_str = super().__str__()
        return base_str + f" A:{self.ability}"


mage = Mage("Merlin", 20, "Fire")
mage.cure()
mage.cure()
print(mage.say())


################################################


# class Transport:
#     def move_to(self):
#         raise NotImplementedError


class Transport:
    def move_to(self):
        return "I can move"


class Radio:
    def listen_radio(self):
        return 'I can listen radio'

    def move_to(self):
        return "I can MOVE"


# class Car(Radio, Transport):
#     pass


class Car(Transport):
    def move_to(self):  # переопределение метода
        return "I can drive"


class Plain(Transport):
    def fly_to(self):
        return "I can fly"


porsche = Car()
print(porsche.move_to())
# print(porsche.listen_radio())

boieng = Plain()
print(boieng.move_to())
print(boieng.fly_to())
