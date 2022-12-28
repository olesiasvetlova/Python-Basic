# task_3
# Ex_1
list_1 = ['Hello', 'hillel', 'how', 'are', 'you']
list_2 = ['hhh', 'llll', 'iiii', '3333']
my_result = []
for i in range(len(list_1)):
    if i % 2 == 0:
        my_result.append(list_1[i])

    else:
        my_result.append(list_2[i])
print(my_result)
# Ex_2
my_result = [list_1[i] for i in range(len(list_1) + 1) if i % 2 == 0] \
            + [list_2[i] for i in range(len(list_2) + 1) if i % 2 != 0]
print(my_result)
# task_11
my_str = 'Hello Hillel, how are you?'
my_list = []
for i in my_str:
    if my_str.count(i) == 1:
        my_list.append(i)
print(my_list)
# task_4
my_list = [1, 3, 5, 6, 7]
new_list = my_list[1:] + [my_list[0]]
print(new_list)
# task_5
my_list = [1, 3, 5, 6, 7]
a = my_list.pop(0)
my_list.append(a)
print(my_list)
# task_6
my_string = '45 больше чем 34 , но меньше чем 100'.split()
count = 0
for i in my_string:
    if i.isdigit():
        count += int(i)
print(count)
# task_7
sting_1 = "My long string"
left = sting_1.find('o')
right = sting_1.rfind('g')
new_string = sting_1[left + 1: right]
print(new_string)
# task_8
string_8 = '/lojuhyftuohk'
list_8 = []
if len(string_8) % 2 != 0:
    string_8 += '_'
for i in range(0, len(string_8), 2):
    list_8.append(string_8[i:i + 2])
print(list_8)
# task_9
list_9 = [2, 4, 1, 5, 3, 9, 0, 7]
count = 0
for i in range(1, len(list_9) - 1):
    if list_9[int(i)] > list_9[int(i) - 1] + list_9[int(i) + 1]:
        count += 1
print(count)
# task_10
list_10 = [1, 2, 3, "11", "22", 33]
new_list_10 = []
for i in list_10:
    if type(i) == str:
        new_list_10.append(i)
print(new_list_10)
