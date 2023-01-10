# task_1
persons = [{'name': 'Lesia', 'age': '80'}, {'name': 'Zenia', 'age': '23'}, {'name': 'Valentina', 'age': '56'},
           {'name': 'Vlada', 'age': '23'}, {'name': 'Oleksandr', 'age': '23'}]
big_name = []
min_age = persons[0]['age']
young_person = []
lenth_name = len(persons[0]['name'])
sum_1 = 0
for i in persons:
    if i['age'] < min_age:
        min_age = i['age']
for i in persons:
    if i['age'] == min_age:
        young_person.append(i['name'])
print(f'Young person are: {young_person}')
for value in persons:
    if len(value['name']) > lenth_name:
        big_name.append(value['name'])
for value in persons:
    sum_1 += int(value['age'])
k = sum_1 // len(persons)
print(f'Longest name are: {big_name}')
print(f'Average number of years of people: {k}')
print()
# task_2
dict_1 = {"name": "Lilia", "age": 25, "lesson": "UK", "country": "Ukraine"}
dict_2 = {"name": "Lesia", "job": "doctor"}
sp_1 = []
for i in dict_1.keys():
    for j in dict_2.keys():
        if i == j:
            sp_1.append(i)
print(sp_1)
sp_2 = [key for key in set(dict_1) - set(dict_2)]
print(sp_2)
dict_3 = dict(i for i in dict_1.items() if i[0] not in dict_2.keys())
print(dict_3)
dict_4 = {}
for i in dict_1.keys() | dict_2.keys():
    if i in dict_1:
        if i in dict_2:
            dict_4[i] = [dict_1[i], dict_2[i]]
        else:
            dict_4[i] = dict_1[i]
    else:
        dict_4[i] = dict_2[i]
print(dict_4)
