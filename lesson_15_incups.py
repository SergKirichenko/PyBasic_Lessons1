# 1. Создать папку ./alphabet/ Если папка существует, то ОК.
# 2. В папке ./alphabet/ создать файлы вида a.txt, b.txt, ..., z.txt
# в которых будет записана строка алфавита, но с заменой буквы из названия файла на прописную.
# Пример: для b.txt строка будет aBcde...
# 3. Сделать щелчек Таноса - удалить случайным образом половину всех файлов в этой папке.

import os
import json
from string import ascii_lowercase as alphabet
from random import shuffle


class PlayWithFolder:
    def __init__(self, dirname):
        self._dirname = dirname
        self.__create_dir()

    @property
    def dirname(self):
        return self._dirname

    def __create_dir(self):
        os.makedirs(self._dirname, exist_ok=True)

    def create_files(self):
        for symbol in alphabet:
            self._create_file(symbol)

    def _create_file(self, symbol):
        file_path = os.path.join(self._dirname, f"{symbol}.txt")
        with open(file_path, 'w') as txt_file:
            txt_file.write(alphabet.replace(symbol, symbol.upper()))

    def do_tannos_click(self):
        dir_list = os.listdir(self._dirname)
        shuffle(dir_list)
        for filename in dir_list[::2]:
            filepath = os.path.join(self._dirname, filename)
            os.remove(filepath)





worker = PlayWithFolder("alphabet_3")
worker.create_files()
print(worker.dirname)
# worker._dirname = "AAA"
# worker._PlayWithFolder__create_dir()
print(dir(worker))
