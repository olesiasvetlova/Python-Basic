#task_1
n = int(input('Enter the number of students: '))
k = int(input('Enter the number of apples: '))
apple_in_scoolchildren = k // n
apple_in_basket = k - (apple_in_scoolchildren * n)
print(f'Available to every student: {apple_in_scoolchildren}')
print(f'Stay in a basket of apples: {apple_in_basket}')
print('\n')
#task_2
class_1 = int(input('Enter the number of students: '))
class_2 = int(input('Enter the number of students: '))
class_3 = int(input('Enter the number of students: '))
desk_in_class = (class_1 // 2 + class_1 % 2) + (class_2 // 2 + class_2 % 2) + (class_3 // 2 + class_3 % 2)
print(f'All you need to buy {desk_in_class} desk')
print('\n')
#task_3
number = int(input('Enter number: '))
number_1 = (number % 10) * 100
number_2 = (number // 10 % 10) * 10
number_3 = number // 100
print(f'{number_1 + number_2 + number_3}')
print('\n')
#task_4
#exemple_1
import time
n = int(input('Enter time: '))
time_format = time.strftime("%H:%M:%S", time.gmtime(n))
print("Time in preferred format:", time_format)
#exempel_2
n = int(input('Enter time: '))
sec = n % (24 * 3600)
hour = n // 3600
sec %= 3600
min = sec // 60
sec %= 60
print(f'{hour}:{min}:{sec}')







