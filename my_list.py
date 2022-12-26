# task_1
import random
my_list = [random.randint(1, 200) for i in range(15)]
for i in my_list:
    if i > 100:
        print(i, end=' ')
print()
# task_2
my_list = [random.randint(1, 200) for i in range(15)]
my_results = []
for i in my_list:
    if i > 100:
        my_results.append(i)
print(my_results)
print()
# task_3
my_list = [random.randint(1, 200) for i in range(5)]
if len(my_list) < 2:
    my_list.append(0)
else:
    if len(my_list) >= 2:
        my_list.append(my_list[-1] + my_list[-2])
print(my_list)
print()
# task_4
my_list = [random.randint(1, 200) for i in range(8)]
print(my_list)
k = int(input('Enter the index of the element in the list: '))
for i in range(k, len(my_list)-1):
    my_list[i] = my_list[i+1]
my_list.pop()
print(my_list)
print()
# task_5
my_list = [random.randint(1, 200) for i in range(8)]
print(my_list)
k = int(input('Enter The index of the element in the list: '))
c = int(input('Enter number: '))
my_list.append(0)
for i in range(len(my_list) - 1, k, -1):
    my_list[i] = my_list[i - 1]
my_list[k] = c
print(my_list)
print()
#task_6
list1 = [3, 7, 9, 5, 4, 33, 11, 23]
list2 = [6, 7, 8, 9, 36, 51, 77, 33]
print(f'Unique numbers: {len(set(list1) & set(list2))}')





