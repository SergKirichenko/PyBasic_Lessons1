# Написать класс и реализовать его методы: (основа - ДЗ № 11)
# - Инициализация класса с одним параметром - имя директории.
#  1. Написать метод экземпляра класса, который создает атрибут экземпляра класса в ввиде словаря
# {'filenames': [список файлов в папке], 'dirnames': [список всех подпапок в папке]}.
# 2. Написать метод экземпляра класса, которая получает булевое значение (True/False).
# Функция возвращает тот же словарь, но с отсортированными именами файлов и папок в соответствующих списках.
# Булевое значение True означает, что порядок сортировки алфавитный, False - обратный порядок.
# 3. Написать метод экземпляра класса, которая получает строку, которая может быть
# или именем файла, или именем папки. (В имени файла должна быть точка).
# В зависимости от того, что функция получила (имя файла или имя папки) - записать его в соответствующий список
# и вернуть обновленный словарь.

import os
from pathlib import Path


class OperationFolder:
    def __init__(self, dirname):
        self.dirname = dirname
        self.dict_directory = self.crate_listdir()

    def __str__(self):
        return f"In your folder: {self.dirname}, has file system : \n .  .  .  .  .   {self.dict_directory} \n"

    def __repr__(self):
        return f"{self.dirname}\n {self.dict_directory}"

    # Метод 1 создает словарь файловой системы в директории экземпляра класса
    def crate_listdir(self) -> dict:  # Create a dict with content folder(dirname)
        file_list = []
        dir_list = []
        for obj_name in Path(self.dirname).iterdir():
            if obj_name.is_file():
                file_list.append(os.path.basename(obj_name))
            elif obj_name.is_dir():
                dir_list.append(os.path.basename(obj_name))
        return {"filenames": file_list, "dirnames": dir_list}

    ##############################################################################################
    # Метод 1(a) (Вариант 2) создает и обновляет словарь файл.сист директории экземпляра класса
    def refresh_listdir(self) -> dict:  # Вариант 2 (по тех. условиям не нужен, но тестирование/работе, полезен)
        self.dict_directory = {"filenames": [os.path.basename(file_name) for file_name in Path(self.dirname).iterdir()
                                             if file_name.is_file()],
                               "dirnames": [os.path.basename(dir_name) for dir_name in Path(self.dirname).iterdir()
                                            if dir_name.is_dir()]}
        return self.dict_directory

    ###############################################################################################

    # Метод 2 сортирует словарь файловой системы папки
    def dict_sorting(self, abc_order=True) -> dict:  # Return sorting self.dict True:alphabet order; False:reverse order
        for key in iter(self.dict_directory):
            self.dict_directory[key] = sorted(self.dict_directory[key], reverse=not abc_order)
        return self.dict_directory

    # Метод 3 добавляет в списки словаря(с файл.сис. директории экземпляра класса), название файла или папки
    # Если таковых нет. Не добавляет одинаковые имена.
    def add_name_to_dict(self, obj_name: str = '') -> dict:  # Return self dict with file/dir
        if "." in obj_name:
            if obj_name not in self.dict_directory["filenames"]:
                self.dict_directory["filenames"].append(obj_name)
        else:
            if obj_name not in self.dict_directory["dirnames"]:
                self.dict_directory["dirnames"].append(obj_name)
        return self.dict_directory

    # 4* (*сдавать не обязательно, но если будете сдавать, то ошибки будут учитываться тоже).
    # Написать метод экземпляра класса, который получает имя директории.
    # Функция проверяет соответствие полученного словаря и реальной файловой системы в полученной папке и,
    # если надо, создает нужные папки и пустые файлы, в соответствии со структурой словаря.
    ##############################################################################################

    #  Метод 4(a)* сравнивает структуры словаря и файловой системы Введенной директории,
    #  И добавляет отсутствующие файлы и папки в директорию.
    def compare_and_assimilate_filesys(self, other_dirname: str) -> None:
        for key in iter(self.dict_directory):
            list_dict = self.dict_directory[key]
            for name_from_dict in list_dict:
                if "." in name_from_dict:
                    file_path = os.path.join(other_dirname, name_from_dict)
                    if not os.path.isfile(file_path):
                        with open(file_path, 'w') as my_file:
                            my_file.write("s")
                else:
                    dir_path = os.path.join(other_dirname, name_from_dict)
                    if not os.path.isdir(dir_path):
                        os.makedirs(dir_path)

    #################################################################################################
    #  Метод 4(b)* сравнивает структуры словаря и файловой системы Введенной директории

    def compare_and_create_objects(self, other_dirname: str):
        folder_objects = crate_listdir(other_dirname)  # Функция вне класса (line 135)
        for filename in set(self.dict_directory["filenames"]).difference(set(folder_objects["filenames"])):
            with open(os.path.join(other_dirname, filename), 'w') as file:
                file.write('')
        for folder_name in set(self.dict_directory["dirnames"]).difference(set(folder_objects["dirnames"])):
            os.makedirs(os.path.join(other_dirname, folder_name))

    ####################################################################################
    #  Дополнительные методы:

    #  функция проверки и создания файла
    def check_and_create_files(self, new_filename: str = "YongFile.txt") -> None:
        file_path = os.path.join(self.dirname, new_filename)
        if not os.path.isfile(file_path):
            with open(file_path, 'w') as my_file:
                my_file.write('s')
        return None

    #  функция проверки и создания директории
    def check_and_create_directories(self, new_dirname: str = "NewFolder") -> None:
        dir_path = os.path.join(self.dirname, new_dirname)
        if not os.path.isdir(dir_path):
            os.makedirs(dir_path)
        return None

    # метод - очистка выбранной папки по вновь добытому списку (!!! удаляет ВСЁ !!! ) (!!!Warning!!! DELETE ALL !!! )
    def clear_at_folder(self):  # Method Clearing in chosen directory
        dict_name = self.crate_listdir()
        list_dict = []
        for key in dict_name.keys():
            list_dict += dict_name[key]
        for names in list_dict:
            file_path = os.path.join(self.dirname, names)
            if os.path.isfile(file_path):
                os.remove(file_path)
        for names in list_dict:
            dir_path = os.path.join(self.dirname, names)
            if os.path.isdir(dir_path):
                os.rmdir(dir_path)


################################################################################
# Создает словарь файловой системы в директории
def crate_listdir(dirname) -> dict:  # Create a dict with content folder(dirname)
    file_list = []
    dir_list = []
    for obj_name in Path(dirname).iterdir():
        if obj_name.is_file():
            file_list.append(os.path.basename(obj_name))
        elif obj_name.is_dir():
            dir_list.append(os.path.basename(obj_name))
    return {"filenames": file_list, "dirnames": dir_list}
