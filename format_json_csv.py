import string
import json
import os
import csv

def cenzor(file: str, list_cenzor: list):
    """
    На вход функция получает имя файла и список слов для замены,
    функция ничего не возвращает, но в результате ее работы необходимо создать файл,
    в котором слова из списка заменены шаблоном(****)
    :return:new_file.txt
    """
    with open(f'{file}.txt', 'r') as some_file:
        word = some_file.read()
        for i in list_cenzor:
            if i in word:
                word = word.replace(i, "****")
        with open('new_file.txt', 'w') as file:
            file.writelines(word)

def count_word(file: str, list_cenzor: list):
    """
    На вход функция получает имя файла и список слов для замены, функция возвращает словарь,
    содержащий в качестве ключей слова, которые были заменены,
    а в качестве значений их количество.
    :return:word_dict
    """
    with open(f'{file}.txt', 'r') as some_file:
        redac_text = some_file.read()
    for i in string.punctuation:
        if i in redac_text.lower():
            redac_text = redac_text.replace(i, '')
    redac_text = redac_text.split()
    word_dict = {}
    for i in list_cenzor:
        word_dict[i] = redac_text.count(i)
    return word_dict

def create_total_list(file: str, dict_of_word: dict):
    """
    На вход функция получает:имя файла, словарь с количеством измененных слов
    Функция возвращает cписок, где ключ - имя файла, значение - словарь с количеством измененных слов
    :param file:
    :param dict_of_word:
    :return:list_of_element
    """
    dict_of_element = {}
    dict_of_element[file] = dict_of_word
    list_of_element = []
    list_of_element.append(dict_of_element)
    print(list_of_element)
    return(list_of_element)

def create_json_file(list_of_dict):
    """
     Функция получает cписок с информацией о фaйле.
    В результате работы создаеться файл stat.json и дописывается информация о новом цензурируемом файле.
    :param list_of_dict:
    :return: stat.json
    """
    if not os.path.isfile('stat.json'):
        with open('stat.json', 'w') as file_json:
            json.dump(list_of_dict, file_json)
    else:
        with open('stat.json', 'r') as file:
            information_on_file = json.load(file)
            information_on_file.append(list_of_dict[0])
        with open('stat.json', 'w') as new_json:
            json.dump(information_on_file, new_json)

def create_csv_file(list_of_dict, file_name_of_text):
    """
    Функция получает cписок с информацией о фaйле и назву файла.
    В результате работы создаеться файл stat.csv и дописывается информация о новом цензурируемом файле.
    :param list_of_dict:
    :param file_name_of_text:
    :return:stat.csv
    """
    if not os.path.isfile('stat.csv'):
        with open('stat.csv', 'w', newline='') as file_csv:
            writer = csv.writer(file_csv, delimiter=';')
            writer.writerow(('name_of_file', 'list_of_word', 'count_word'))
    with open('stat.csv', 'a', newline='') as new_csv:
        writer = csv.writer(new_csv, delimiter=';')
        writer.writerow((f'{file_name_of_text}', '', ''))
    for key, value in list_of_dict[0][f'{file_name_of_text}'].items():
        with open ('stat.csv', 'a', newline='') as file_on_csv:
            writer = csv.writer(file_on_csv, delimiter=';')
            writer.writerow(('', key, value))













