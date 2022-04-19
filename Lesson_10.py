#
# 1. Написать функцию, которая получает в виде параметра имя файла названия интернет доменов (domains.txt)
# и возвращает их в виде списка строк (названия возвращать без точки).
import datetime


def open_file(filename) -> str:
    with open(filename, 'r') as my_file:
        data = my_file.read()
    return data


def domain_without_point(filename):
    data_str = open_file(filename)
    result_domains = [domain[1:] for domain in data_str.split("\n")]
    return result_domains


exercise_1 = domain_without_point('domains.txt')
print("2- ", exercise_1)


# 2. Написать функцию, которая получает в виде параметра имя файла (names.txt)
# и возвращает список всех фамилий из него.
# Каждая строка файла содержит номер, фамилию, страну, некоторое число (таблица взята с википедии).
# Разделитель - символ табуляции "\t"


def getting_surnames(filename) -> list:
    data_str = open_file(filename)
    data_list = data_str.split("\n")
    surnames_list = []
    for words_str in data_list:
        words_list = words_str.split("\t")
        surnames_list.append(words_list[1])
    return surnames_list


exercise_2 = getting_surnames("names.txt")
print("2- ", exercise_2)


#  Это случайное дополнительное задание "получение списка фамилий авторов" во 2-ом задании для файла authors.txt
def getting_list_surnames_of_authors(filename) -> list:
    data_str = open_file(filename)
    surnames_list = []
    data_list = data_str.split("\n")
    data_line_str = " ".join(data_list)
    words_list_data = data_line_str.split(' ')
    for words_str in words_list_data:
        if "'s" in words_str:
            spec_words_str = words_str[:-2]
            if spec_words_str.istitle():
                surnames_list.append(spec_words_str)
    result = list(set(surnames_list))
    return result


exercise_2_plus = getting_list_surnames_of_authors('authors.txt')
print("2+ -", exercise_2_plus)


# 3. Написать функцию, которая получает в виде параметра имя файла (authors.txt) и возвращает список
# словарей вида {"date": date}
# в которых date - это дата из строки (если есть),
# Например [{"date": "1st January 1919"}, {"date": "8th February 1828"},  ...]


def list_date_dictionaries(filename) ->list:
    data = open_file(filename)
    data_list = data.split("\n")
    data_len_sort = [my_str for my_str in data_list if len(my_str) > 12]
    list_with_date = []
    for data_str in data_len_sort:
        list_sort = data_str.split(" - ")
        list_with_date.append({"data": list_sort[0]})
    return list_with_date


exercise_3 = list_date_dictionaries("authors.txt")
print("3- ", exercise_3)


#  По просьбам некоторых студентов, начну включать дополнительные задания.
# 4* (*сдавать не обязательно, но если будете сдавать, то ошибки будут учитываться тоже).
# Написать функцию, которая получает в виде параметра имя файла (authors.txt) и возвращает список
# словарей вида {"date_original": date_original, "date_modified": date_modified}
# в которых date_original - это дата из строки (если есть),
# а date_modified - эта же дата, представленная в формате "dd/mm/yyyy" (d-день, m-месяц, y-год)
# Например [{"date_original": "8th February 1828", "date_modified": 08/02/1828},  ...]

# Подготовительная функция (мануальный способ):
def modification_date(date_str) -> str:
    months_dict = {"January": "01",
                   "February": "02",
                   "March": "03",
                   "April": "04",
                   "May": "05",
                   "June": "06",
                   "July": "07",
                   "August": "08",
                   "September": "09",
                   "October": "10",
                   "November": "11",
                   "December": "12"}

    date_list = date_str.split(' ')
    days = date_list[0][:-2] if len(date_list) >= 3 else ""
    years = date_list[2] if len(date_list) >= 3 else date_list[1]
    months = months_dict[date_list[1]] if len(date_list) >= 3 else months_dict[date_list[0]]
    modified_date = f"{days}/{months}/{years}"
    return modified_date


# Подготовительная функция (c помощью модуля datatime):
def converting_date(date_str) -> str:
    date_list = date_str.split(' ')
    if len(date_list) >= 3:
        day_str = date_list[0]
        str_date = (day_str[0:-2]) + (" ".join(date_list[1:3]))
        convert_date = datetime.datetime.strptime(str_date, "%d%B %Y").strftime('%d/%m/%Y')
    else:
        convert_date = datetime.datetime.strptime(date_str, "%B %Y").strftime('/%m/%Y')
    return convert_date


#  Основная функция (с мануальной функцией)
def modify_date_list_dictionaries(filename) -> list:
    original_date_dict = list_date_dictionaries(filename)  # вызов функции задания 3
    data_list = []
    for my_dict in original_date_dict:
        date_words_str = my_dict["data"]
        modify_date = modification_date(date_words_str)  # вызов подготовительно функции
        data_list.append({"date_original": my_dict["data"], "date_modified": modify_date})
    return data_list


exercise_4a = modify_date_list_dictionaries("authors.txt")
print("4a- ", exercise_4a)


#  Основная функция (с функцией через datetime)
def convert_date_list_dictionaries(filename) -> list:
    original_date_dict = list_date_dictionaries(filename)  # вызов функции задания 3
    data_list = []
    for my_dict in original_date_dict:
        date_words_str = my_dict["data"]
        modify_date = converting_date(date_words_str)  # вызов подготовительно функции
        data_list.append({"date_original": my_dict["data"], "date_modified": modify_date})
    return data_list


exercise_4b = convert_date_list_dictionaries("authors.txt")
print("4b-", exercise_4b)
