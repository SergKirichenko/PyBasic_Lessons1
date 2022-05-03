# Все пункты являются частью одного задания, поэтому можно использовать функции несколько раз и не дублировать код.
# Если хотите, можете использовать значения по умолчанию и аннотацию типов.

# 1. Написать функцию, которая получает один параметр - имя директории и возвращает словарь вида
# {'filenames': [список файлов в папке], 'dirnames': [список всех подпапок в папке]}.
# Подпапки учитывать только первого уровня вложения. Папка в папке в папке - такое не брать ))
#
import os
from pathlib import Path


def view_dirlist(dirname: str) -> dict:  # Вариант 1
    dir_list = os.listdir(dirname)
    os.chdir(dirname)  # вход в директорию для проверки
    dict_dirlist = {"filenames": [file_name for file_name in dir_list if os.path.isfile(file_name)],
                    # это пример увеличивает количество дествий в 2 раза
                    "dirnames": [dir_name for dir_name in dir_list if os.path.isdir(dir_name)]}
    os.chdir("..")  # выход из директории
    return dict_dirlist


def view_listdir_with_path(dirname: str) -> dict:  # Вариант 2
    dirlist_2 = {"filenames": [os.path.basename(file_name) for file_name in Path(dirname).iterdir()
                               if file_name.is_file()],
                 "dirnames": [os.path.basename(dir_name) for dir_name in Path(dirname).iterdir()
                              if dir_name.is_dir()]}
    return dirlist_2


dict_dir_and_file_names_v1 = view_dirlist('TEST')  # Вызов варианта 1

dict_dir_and_file_names_v2 = view_listdir_with_path('TEST')  # Вызов варианта 2

print("1-A", dict_dir_and_file_names_v1)

print("1-B", dict_dir_and_file_names_v2)


# 2. Написать функцию, которая получает два параметра - словарь, описанный в пункте 1
# и булевое значение (True/False) - можно сделать параметром по умолчанию.
# Функция возвращает тот же словарь, но с отсортированными именами файлов и папок в соответствующих списках.
# Булевое значение True означает, что порядок сортировки алфавитный, False - обратный порядок.
#


def dict_sorting(dict_name: dict, bool_name=True) -> dict:
    for key in iter(dict_name):
        dict_name[key] = sorted(dict_name[key], reverse=not bool_name)
    return dict_name


sort_dict = dict_sorting(dict_dir_and_file_names_v1, False)
print("2 -", sort_dict)


# 3. Написать функцию, которая получает два параметра - словарь, описанный в пункте 1 и строку, которая может быть
# или именем файла, или именем папки. (В имени файла должна быть точка).
# В зависимости от того, что функция получила (имя файла или имя папки) - записать его в соответствующий список
# и вернуть обновленный словарь.


def add_name_to_dict(dict_name: dict, obj_name: str) -> dict:
    if "." in obj_name:
        dict_name["filenames"].append(obj_name)
    else:
        dict_name["dirnames"].append(obj_name)
    return dict_name


add_file = add_name_to_dict(dict_dir_and_file_names_v1, "qwerty.txt")  # Вызов 1: Добавлен файл
add_dir = add_name_to_dict(dict_dir_and_file_names_v1, "Dir_ABC")  # Вызов 2: Добавлен каталог/папка/директория
print("3 -", add_dir)


# 4* (*сдавать не обязательно, но если будете сдавать, то ошибки будут учитываться тоже).
# Написать функцию, которая получает два параметра - словарь, описанный в пункте 1 и имя директории.
# Функция проверяет соответствие полученного словаря и реальной файловой системы в полученной папке и,
# если надо, создает нужные папки и пустые файлы, в соответствии со структурой словаря.

#  функция проверки и создания файла
def check_and_create_files(other_dir_name: str, filename: str) -> None:
    file_path = os.path.join(other_dir_name, filename)
    if not os.path.isfile(file_path):
        with open(file_path, 'w') as my_file:
            my_file.write("s")
    return None


#  функция проверки и создания директории
def check_and_create_directories(other_dir_name: str, sub_dirname: str) -> None:
    dir_path = os.path.join(other_dir_name, sub_dirname)
    if not os.path.isdir(dir_path):
        os.makedirs(dir_path)
    return None


#  функция сравнения структуры словаря и файловой системы директории
def compare_and_assimilate_filesys(dict_name: dict, other_dir_name: str) -> None:
    for key in iter(dict_name):
        list_dict = dict_name[key]
        for name_from_dict in list_dict:
            if "." in name_from_dict:
                check_and_create_files(other_dir_name, name_from_dict)
            else:
                check_and_create_directories(other_dir_name, name_from_dict)
    return None


compare_and_assimilate_filesys(dict_dir_and_file_names_v1, "ABCDEF")


################################################################################

def compare_and_create_objects(dict_directory: dict, other_dirname: str):
    folder_objects_real = view_listdir_with_path(other_dirname)
    for filename in set(dict_directory["filenames"]).difference(set(folder_objects_real["filenames"])):
        with open(os.path.join(other_dirname, filename), 'w') as file:
            file.write('')
    for folder in set(dict_directory["dirnames"]).difference(set(folder_objects_real["dirnames"])):
        os.makedirs(os.path.join(other_dirname, folder))
