#
import string
import random


# 1. Написать функцию которой передается один параметр - список строк my_list.
# Функция возвращает новый список в котором содержаться
# элементы из my_list по следующему правилу:
# Если строка стоит на нечетном месте в my_list, то ее заменить на
# перевернутую строку. "qwe" на "ewq".
# Если на четном - оставить без изменения.
#
def change_odd_str(my_list):
    result = [(symbol[::-1] if index % 2 else symbol) for index, symbol in enumerate(my_list)]
    return result


my_list_1 = ["qwerty", "asdfgh", "zxcvbn", "12345", ]

odd_str = change_odd_str(my_list_1)


# 2. Написать функцию которой передается один параметр - список строк my_list.
# Функция возвращает новый список в котором содержаться
# элементы из my_list у которых первый символ - буква "a".
#
def chooses_with_first_a(my_list):
    result = [symbol for symbol in my_list if symbol[0] == "a"]
    return result


my_list_2 = ["qwerty", "asdfgh", "zxcvbn", "12345", ]
list_432 = ["aaa", "bbb", "ccc", "abc", ]

first_a = chooses_with_first_a(list_432)


# 3. Написать функцию которой передается один параметр - список строк my_list.
# Функция возвращает новый список в котором содержаться
# элементы из my_list в которых есть символ - буква "a" на любом месте.
#
def chooses_with_a(my_list):
    result = [symbol for symbol in my_list if "a" in symbol]
    return result


my_list_3 = ["qwerty", "asdfgh", "zxcvbn", "12345", "zcadqe", ]

with_a = chooses_with_a(my_list_3)


# 4. Написать функцию которой передается один параметр - список строк my_list в
# котором могут быть как строки (type str) так и целые числа (type int).
# Функция возвращает новый список в котором содержаться только строки из my_list.
#

def filter_with_str_only(my_list):
    result = [item for item in my_list if type(item) == str]
    return result


my_list_4 = [3, 4, 7, 12, "gcs", "sdc", "res", ]

str_only = filter_with_str_only(my_list_4)


# 5. Написать функцию которой передается один параметр - строка my_str.
# Функция возвращает новый список в котором содержаться те символы из my_str,
# которые встречаются в строке только один раз.
#


def filter_for_single_symbol(my_str):
    result = [symbol for symbol in set(my_str) if my_str.count(symbol) == 1]
    return result


my_str_5 = "sasssssssssssssddddddaaaaaaaaaaaagjlsaatrxxx"

single_symbol = filter_for_single_symbol(my_str_5)

# 6. Написать функцию которой передается два параметра - две строки.
# Функция возвращает список в который поместить те символы,
# которые есть в обеих строках хотя бы раз.
#


def find_same_symbol(my_str_1, my_str_2):
    result = list(set(my_str_1).intersection(set(my_str_2)))
    return result


my_str_A = "qazwsxxxxxxx"
my_str_B = "qwertyxxxxxx"

same_symbol = find_same_symbol(my_str_A, my_str_B)


# 7. Написать функцию которой передается два параметра - две строки.
# Функция возвращает список в который поместить те символы, которые есть в обеих строках,
# но в каждой только по одному разу.
#

def find_same_single_symbol(my_str_1, my_str_2):
    my_result = []
    for symbol in set(my_str_1).intersection(set(my_str_2)):
        if my_str_1.count(symbol) == 1 and my_str_2.count(symbol) == 1:
            my_result.append(symbol)
    return my_result


my_str_a = "qqqqaaaaaaaaaaaazzzwsxjhy"
my_str_b = "qqqwwwwwaasszxjpo"

symbol_at_one = find_same_single_symbol(my_str_a, my_str_b)

# 8. Даны списки names и domains (создать самостоятельно).
# Написать функцию для генерирования e-mail в формате:
# фамилия.число_от_100_до_999@строка_букв_длинной_от_5_до_7_символов.домен
# фамилию и домен брать случайным образом из заданных списков переданных в функцию в виде параметров.
# Строку и число генерировать случайным образом.
#
# Пример использования функции:
# names = ["king", "miller", "kean"]
# domains = ["net", "com", "ua"]
# e_mail = create_email(domains, names)
# print(e_mail)
# >>>miller.249@sgdyyur.com
#################################################


def generate_email(domain, name):
    mu_str = "".join(random.sample(string.ascii_lowercase, random.choice([6, 5, 7])))
    mail = random.choice(name) + str(random.randint(100, 999)) + "@" + mu_str + random.choice(domain)
    return mail


names = ["Smith", "Ocean", "Lynch", "Stone", ]
domains = [".com", ".net", ".ua", ".pl", ]

email = generate_email(domains, names)

#############################################
print("1", odd_str)
print("2", first_a)
print("3", with_a)
print("4", str_only)
print("5", single_symbol)
print("6", same_symbol)
print("7", symbol_at_one)
print("8", email)
