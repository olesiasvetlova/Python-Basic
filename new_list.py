def task_1(my_list: list) -> list:
    """
    Функция возвращает новый список в котором:
    Если строка стоит на нечетном месте в my_list, то ее заменить на
    перевернутую строку. "qwe" на "ewq".
    Если на четном - оставить без изменения.
    :param my_list:
    :return: result
    """
    result = []
    for index in range(len(my_list)):
        if index % 2 != 0:
            result.append(my_list[index][::-1])
        else:
            result.append(my_list[index])
    return result


def task_2(my_list_2: list) -> list:
    """
    Функция возвращает новый список в котором содержаться
    элементы из my_list, у которых первый символ - буква "a"
    :param my_list_2:
    :return: new_list_2
     """
    new_list_2 = [i for i in my_list_2 if i[0] == 'a' or i[0] == 'A']
    return new_list_2


def task_2_1(my_list_2: list) -> list:
    sp = []
    for i in my_list_2:
        if i.lower().startwith('a'):
            sp.append(i)
        return sp


def a_finder(data: list) -> list:
    """
    Функция возвращает новый список в котором содержаться
    элементы из my_list в которых есть символ - буква "a" на любом месте.
    :param data:
    :return:result
    """
    result = []
    for string in data:
        if 'A' in string.upper():
            result.append(string)
    return result


def task_4(my_list_4: list) -> list:
    """
    Функция возвращает новый список в котором
    содержаться только строки из my_list.
    :param my_list_4:
    :return: new_list4
    """
    new_list4 = [i for i in my_list_4 if type(i) == str]
    return new_list4


def task_5(my_str: str) -> list:
    """
    Функция возвращает новый список в котором
    содержаться те символы из my_str,
    которые встречаются в строке только один раз.
    :param my_str:
    :return:new_list5
    """
    new_list5 = [i for i in my_str if my_str.count(i) == 1]
    return new_list5


def task_6(my_str: str, my_str_1: str) -> list:
    """
    Функция возвращает список в который поместить те символы,
    которые есть в обеих строках хотя бы раз.
    :param my_str_1:
    :param my_str:
    :return:new_list_6
    """
    new_list_6 = [i for i in set(my_str + my_str_1) if i in my_str and i in my_str_1]
    return new_list_6


def task_7(my_str: str, my_str_1: str) -> list:
    """
    Функция возвращает список в который поместить
    те символы, которые есть в обеих строках,
    но в каждой только по одному разу.
    :param my_str_1:
    :param my_str:
    :return:new_list_7
    """
    sp_1 = [i for i in my_str if my_str.count(i) == 1]
    sp_2 = [i for i in my_str_1 if my_str_1.count(i) == 1]
    new_list_7 = list(set(sp_1) & set(sp_2))
    return new_list_7
