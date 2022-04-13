#####################################################
# 1. Дано целое число (int). Определить сколько нулей в этом числе.
# 1 ##################################################

number_1 = 14602604908
# result_1 = str(number_1).count("0")

number_str = str(number_1)  #
result_1 = number_str.count("0")  #

print("1- ", result_1)

# 2. Дано целое число (int). Определить сколько нулей в конце этого числа. Например, для числа 1002000 - три нуля
# 2 ##################################################

number_2 = 1200460100
half_result = int(str(number_2)[::-1])
result_2 = len(str(number_2)) - len(str(half_result))
print("2- ", result_2)

# 3. Даны списки my_list_1 и my_list_2.
# Создать список my_result в который вначале поместить
# элементы на четных местах из my_list_1, а потом все элементы на нечетных местах из my_list_2.
#####
# Создать список my_result в который вначале поместить
# элементы с четных мест my_list_1, а потом все элементы с нечетных мест my_list_2.
# 3  ##################################################

my_list_1 = list("012345")
my_list_2 = list("ZXCVBN2")
my_result = my_list_1[::2] + my_list_2[1::2]
print("3- ", my_result)

# 4. Дан список my_list. СОЗДАТЬ НОВЫЙ список new_list у которого первый элемент из my_list
# стоит на последнем месте. Если my_list [1,2,3,4], то new_list [2,3,4,1]
# 4 #########################################################

my_list_4 = list("a1234z")
new_list = my_list_4[1:] + [my_list_4[0]]
# new_list.append(my_list_4[0])
print("4- ", new_list)

# 5.Дан список my_list. В ЭТОМ списке первый элемент переставить на последнее место.
# [1,2,3,4] -> [2,3,4,1]. Пересоздавать список нельзя! (используйте метод pop)
# 5 ########################################################

my_list_5 = [1, 2, 3, 4, 5, ]
# value = my_list_5.pop(0)
my_list_5.append(my_list_5.pop(0))
print("5- ", my_list_5)

# 6. Дана строка в которой есть числа (разделяются пробелами).
# Например "43 больше чем 34, но меньше чем 56". Найти сумму ВСЕХ ЧИСЕЛ (А НЕ ЦИФР) в этой строке.
# Для данного примера ответ - 133. (используйте split и проверку isdigit)
# 6 #######################################################

my_str = "14 32  1 7"
my_str_list = my_str.split()
value = 0
for item in my_str_list:
    if item.isdigit():
        value += int(item)
print("6- ", value)

# 7. Дана строка my_str в которой символы МОГУТ повторяться и два символа l_limit, r_limit,
# которые точно находятся в этой строке. Причем l_limit левее чем r_limit.
# В переменную sub_str поместить НАИБОЛЬШУЮ часть строки между этими символами.
# my_str = "My long string", l_limit = "o", r_limit = "g" -> sub_str = "ng strin".
# 7 ############################################################

my_str = "It wonderful time, bla bla bla."
l_limit = "o"
r_limit = "b"
# index_a = my_str.find(l_limit) + 1
# index_b = my_str.rfind(r_limit)
sub_str = my_str[my_str.find(l_limit) + 1:my_str.rfind(r_limit)]
print("7- ", sub_str)

# 8. Дана строка my_str. Разделите эту строку на пары из двух символов и поместите эти пары в список.
# Если строка содержит нечетное количество символов, пропущенный второй символ последней пары должен
# быть заменен подчеркиванием ('_'). Примеры: 'abcd' -> ['ab', 'cd'], 'abcde' -> ['ab', 'cd', e_']
# (используйте срезы длинны 2)
# 8 #############################################################
my_str = "werty123zxcvb456asd"
result_8 = []
if len(my_str) % 2:
    my_str += "_"
#  1й Вариант  ############################################
# index_A = 0
# index_B = 2
# for index in range(int(len(my_str) / 2)):
#     symbol = my_str[index_A:index_B]
#     result_8.append(symbol)
#     index_A += 2
#     index_B += 2
# 2й вариант  ######################################
index = 0
while index < len(my_str):
    symbol = my_str[index:(index + 2)]
    result_8.append(symbol)
    index += 2
#########################################
print("8- ", result_8)
#########################################

# 9. Дан список чисел. Определите, сколько в этом списке элементов,
# которые больше суммы двух своих соседей (слева и справа), и НАПЕЧАТАЙТЕ КОЛИЧЕСТВО таких элементов.
# Крайние элементы списка никогда не учитываются, поскольку у них недостаточно соседей.
# Для списка [2,4,1,5,3,9,0,7] ответом будет 3 потому что 4 > 2+1, 5 > 1+3, 9>3+0.
# 9 ##############################################################

my_list_9 = [3, 5, 1, 8, 4, 6, 11, 3, ]
my_res = []
for index in range(1, len(my_list_9) - 1):
    if my_list_9[index] > (my_list_9[index - 1] + my_list_9[index + 1]):
        my_res.append(my_list_9[index])
result_9 = len(my_res)  #

# result_9 = len([my_list_9[index] for index in range(1, len(my_list_9) - 1)
#                 if my_list_9[index] > (my_list_9[index - 1] + my_list_9[index + 1])])

print("9- ", result_9)

# 10. Дан список my_list в котором могут быть как строки (type str) так и целые числа (type int).
# Например [1, 2, 3, "11", "22", 33]
# Создать новый список в который поместить только строки из my_list.
# 10 ##############################################################

my_list_10 = [3, 4, 7, 12, "3", "23", "32", ]
my_result_10 = [item for item in my_list_10 if type(item) == str]

print("10- ", my_result_10)

# 11. Дана строка my_str. Создать список в который поместить те символы, из my_str,
# которые встречаются в строке ТОЛЬКО ОДИН раз.
# 11 ###############################################################

my_str = "sasssssssssssssddddddaaaaaaaaaaaagjlsaatrxxx"
my_list_result_11 = []

my_set = set(my_str)

for symbol in my_set:  # Вариант 1
    item = my_str.count(symbol)  #
    if item == 1:  #
        my_list_result_11.append(symbol)  #

my_result_11_v2 = [symbol for symbol in set(my_str) if my_str.count(symbol) == 1]  # Вариант 2

print("11- ", my_list_result_11, ",V 2 -", my_result_11_v2)

# 12. Даны две строки. Создать список в который поместить те символы,
# которые есть в обеих строках хотя бы раз.
# 12 #################################################

my_str_A = "qazwsxxxxxxx"
my_str_B = "qwertyxxxxxx"

# my_result_12 = [symbol for symbol in my_str_A if symbol in my_str_B]  # Вариант 1,
my_result_12_set = list(set(my_str_A).intersection(set(my_str_B)))  # Вариант 2,

print("12- ", my_result_12_set)

# 13. Даны две строки. Создать список в который поместить те символы, которые есть в обеих строках,
# но в каждой ТОЛЬКО ПО ОДНОМУ разу.
# Пример: для строк "aaaasdf1" и "asdfff2" ответ ["s", "d"], т.к. эти символы есть в каждой строке по одному разу
# 13 ##########################################################

my_str_1 = "qqqqaaaaaaaaaaaazzzwsxj"
my_str_2 = "qqqwwwwwaasszxj"
my_result_13 = []
for symbol in set(my_str_1).intersection(set(my_str_2)):
    if my_str_1.count(symbol) == 1 and my_str_2.count(symbol) == 1:
        my_result_13.append(symbol)
#####################################################
print("13- ", my_result_13)
##################################################
