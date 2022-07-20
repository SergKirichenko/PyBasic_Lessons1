# ООП
# класс
# экземпляр класса  - "self"
# атрибут класса
# атрибут экземпляра класса
from typing import Optional


class Person:  # класс
    name: Optional[str] = None  # атрибут класса
    age: int = 0
    job: dict = {"title": "Programmer", "company": "GoWombat"}


person_1 = Person()  # экземпляр класса (представитель объекта)
person_2 = Person()

person_1.name = "John"  # атрибут экземпляра класса
person_1.age = 23  # атрибут экземпляра класса

person_2.name = "Anna"  # атрибут экземпляра класса
person_2.age = 30  # атрибут экземпляра класса
person_2.gender = 'female'  # добавили атрибут в экземпляр класса

person_3 = Person()
Person.name = "Jack"
person_4 = Person()

print(person_1.name, person_1.age)
print(person_2.name, person_2.age, person_2.gender)
print(person_3.name, person_3.age)
print(person_4.name, person_4.age, person_4.job["company"])

############################################################################

class Person:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
        self.name_uppercase = self.get_name_uppercase()

    def __str__(self):
        return f"I'm {self.name}, i'm {self.age}"

    def __repr__(self):
        return f"{self.name_uppercase}"

    def increase_age(self):
        self.age += 1

    def get_name_uppercase(self):
        name_uppercase = self.name.upper()
        return name_uppercase


my_name = "Vova"
my_age = 42

zontov = Person(my_name, my_age)
print(zontov)

person_1 = Person(name="Adam", age=23)
print(person_1.name, person_1.age)

person_2 = Person(name="Eva", age=23)
print(person_2)

person_1.increase_age()
persons = [person_1, person_2]
print(persons)


# 1. Создать папку ./alphabet/ Если папка существует, то ОК.
# 2. В папке ./alphabet/ создать файлы вида a.txt, b.txt, ..., z.txt
# в которых будет записана строка алфавита, но с заменой буквы из названия файла на прописную.
# Пример: для b.txt строка будет aBcde...
# 3. Сделать щелчек Таноса - удалить случайным образом половину всех файлов в этой папке.

import os
from string import ascii_lowercase as alphabet
from random import shuffle


class PlayWithFolder:
    def __init__(self, dirname):
        self.dirname = dirname
        self.create_dir()

    def create_dir(self):
        os.makedirs(self.dirname, exist_ok=True)

    def create_files(self):
        for symbol in alphabet:
            self.create_file(symbol)

    def create_file(self, symbol):
        file_path = os.path.join(self.dirname, f"{symbol}.txt")
        with open(file_path, 'w') as txt_file:
            txt_file.write(alphabet.replace(symbol, symbol.upper()))

    def do_tannos_click(self):
        dir_list = os.listdir(self.dirname)
        shuffle(dir_list)
        for filename in dir_list[::2]:
            filepath = os.path.join(self.dirname, filename)
            os.remove(filepath)


worker = PlayWithFolder("alphabet_2")
worker.create_files()
