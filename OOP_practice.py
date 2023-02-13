import os


class Dir_name:

    def __init__(self, dir_name):  # инициализация класса с одним параметром - имя директории.
        self.name = dir_name

    def get_dir_consist(self):  # метод класса, который создает атрибут класса в ввиде словаря
        # {'filenames': [список файлов в папке], 'dirnames': [список всех подпапок в папке]}.
        dirs = list()
        files = list()
        for i in os.listdir(self.name):
            if os.path.isdir(i):
                dirs.append(i)
            else:
                files.append(i)
        self.content = {'filenames': files, 'dirnames': dirs}

    def sort(self, reverse):  # метод класса, которий получает булевое значение (True/False).
        # Функция возвращает тот же словарь, но с отсортированными именами файлов и папок в соответствующих списках.
        if isinstance(reverse, bool):
            self.content['filenames'].sort(reverse=reverse)
            self.content['dirnames'].sort(reverse=reverse)
            return self.content
        else:
            print('Input data can be only Bool')

    def add_i(self, i):  # метод класса, которий получает строку, которая может быть
        # или именем файла, или именем папки. (В имени файла должна быть точка).
        # В зависимости от того, что функция получила (имя файла или имя папки) - записать его
        # в соответствующий список и вернуть обновленный словарь.
        if '.' in i[1:]:
            self.content['filenames'].append(i)
        else:
            self.content['dirnames'].append(i)
        return self.content


directoty = Dir_name((os.getcwd()))
directoty.get_dir_consist()
print(directoty.content)
print(directoty.add_i('rest'))
print(directoty.add_i('rest.txt'))
print(directoty.add_i('.rest'))