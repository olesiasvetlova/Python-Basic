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


list_words = ["never", "been"]
cenzor('text', list_words)

import string


def count_word():
    """
    На вход функция получает имя файла, функция возвращает словарь,
    содержащий в качестве ключей слова из текстового файла, а в качестве значений их количество.
    Орфографические символы не учитывать, регистр не учитывать(The == the)
    :return:word_dict
    """

    with open('text.txt', 'r') as some_file:
        word = some_file.read()
    for i in string.punctuation:
        if i in word.lower():
            word = word.replace(i, '')
    word = word.split()
    unic_word = set(word)
    word_dict = {}
    for i in unic_word:
        word_dict[i] = word.count(i)
    print(word_dict)


count_word()
