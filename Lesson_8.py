#########################################################################
# 1. Дан список строк my_list. Создать новый список в который поместить
# элементы из my_list по следующему правилу:
# Если строка стоит на нечетном месте в my_list, то ее заменить на
# перевернутую строку. "qwe" на "ewq".
# Если на четном - оставить без изменения.
# Задание сделать с использованием enumerate или range.
# 1 #####################################################################

my_list = ["qwerty", "asdfgh", "zxcvbn", "12345", ]

# my_result_a = []  # Вариант А
# for index in range(len(my_list)):
#     if index % 2:
#         revers_list = my_list[index]
#         my_result_a.insert(index, revers_list[::-1])
#     else:
#         my_result_a.insert(index, my_list[index])

my_result_b = []  # Вариант Б
for index, symbol in enumerate(my_list):
    if index % 2:
        my_result_b.append(symbol[::-1])
    else:
        my_result_b.append(symbol)

print("1- (a)", my_result_b, "\n")

# 2. Дан список строк my_list. Создать новый список в который поместить
# элементы из my_list у которых первый символ - буква "a".
# 2 #######################################################################

my_list = ["qwerty", "asdfgh", "zxcvbn", "12345", ]  # Вариант А
my_result_2a = []  #
for symbol in my_list:  #
    if symbol[0] == "a":  #
        my_result_2a.append(symbol)  #

my_result_2b = [symbol for symbol in my_list if symbol[0] == "a"]  # Вариант Б

print("2- (a)", my_result_2a, "\n2- (b)", my_result_2b, "\n")

# 3. Дан список строк my_list. Создать новый список в который поместить
# элементы из my_list в которых есть символ - буква "a" на любом месте.
# 3 #######################################################################

my_list = ["qwerty", "asdfgh", "zxcvbn", "12345", "zcadqe", ]

my_result_3a = [symbol for symbol in my_list if "a" in symbol]

print("3- (I)", my_result_3a, "\n")

# 4) Дан список словарей persons в формате [{"name": "John", "age": 15}, ... ,{"name": "Jack", "age": 45}]
# а) Создать список и поместить туда имя самого молодого человека.
#    Если возраст совпадает - поместить все имена самых молодых.
# б) Создать список и поместить туда самое длинное имя. Если длина имени совпадает - поместить все такие имена.
# в) Посчитать среднее количество лет всех людей из начального списка.
# 4 #############################################################################

person = [{"name": "John", "age": 21},
          {"name": "William", "age": 32},
          {"name": "Alise", "age": 17},
          {"name": "Jack", "age": 41},
          ]
name_of_person = [person_name.get("name") for person_name in person]
age_of_person = [person_age.get("age") for person_age in person]
min_age = min(age_of_person)
middle_ages = sum(age_of_person) / len(age_of_person)

youngest_man = []
for index in person:
    level = index.get("age")
    if level == min_age:
        youngest_man.append(index["name"])

name_max_len = []
max_len_name = max([len(symbol) for symbol in name_of_person])
for symbol in name_of_person:
    item = len(symbol)
    if item == max_len_name:
        name_max_len.append(symbol)

print("4- (A):", youngest_man)
print("4- (Б):", name_max_len)
print("4- (B):", middle_ages, "\n")

# 5) Даны два словаря my_dict_1 и my_dict_2.
# а) Создать список из ключей, которые есть в обоих словарях.
# б) Создать список из ключей, которые есть в первом, но нет во втором словаре.
# в) Создать новый словарь из пар {ключ:значение}, для ключей, которые есть в первом, но нет во втором словаре.
# г) Объединить эти два словаря в новый словарь по правилу:
# если ключ есть только в одном из двух словарей - поместить пару {ключ:значение},
# если ключ есть в двух словарях - поместить пару {ключ: [значение_из_первого_словаря, значение_из_второго_словаря]},
#
# {1:1, 2:2}, {11:11, 2:22} ---> {1:1, 11:11, 2:[2, 22]}

# 5 ######################################################################

my_dict_1 = {"name": "Bill",
             "age": 36,
             "Auto": "Honda",
             "Job": "Artist",
             }
my_dict_2 = {"name": "Olivia",
             "age": 29,
             "Moto": "Suzuki",
             "Hobby": "paint",
             }

list_key_A = list(set(my_dict_1.keys()).intersection(set(my_dict_2.keys())))
print("5- (A):", list_key_A)

list_key_B = list(set(my_dict_1.keys()).difference(set(my_dict_2.keys())))
print("5- (Б):", list_key_B)

my_dict_3a = {index: (my_dict_1[index]) for index in list_key_B}
print("5- (B):", my_dict_3a)

my_dict_4 = {}
my_dict_4.update(my_dict_2)

for key, value in my_dict_1.items():
    if my_dict_2.get(key, 0):
        my_dict_4[key] = [value, my_dict_2[key]]
    else:
        my_dict_4[key] = value

print("5- (Г):", my_dict_4)
