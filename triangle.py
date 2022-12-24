# # task_1
my_string = '0123456789'
for i in my_string:
    for j in my_string:
        if i == '0':
            print(f'{int(j)}', end=' ')
            continue
        print(f'{int(i)}{int(j)}', end=' ')
print()
# #task_2
n = int(input('Enter altitude share: '))
for i in range(1, n + 1):
    # printing spaces
    for j in range(n - i):
        print(' ', end=' ')
    # printing stars
    for k in range(2 * i - 1):
        # print star at start and end of the row
        if k == 0 or k == 2 * i - 2:
            print('*', end=' ')
        else:
            if i == n:
                print('*', end=' ')
            else:
                print(' ', end=' ')
    print()
print()
for i in range(1, n + 1):
    for j in range(n * 2 - i * 2):
        print(' ', end='')
    for k in range(2 * i - 1):
        print('*', end=' ')
    print()
print()
for i in range(1, n + 1):
    for j in range(n * 2 - i * 2):
        print(' ', end='')
    for k in range(2 * i - 1):
        print('*', end=' ')
    print()
for i in range(n - 1):
    for j in range(i + 1):
        print(' ', end=' ')
    for j in range(2 * (n - i - 1) - 1):
        if j == 0 or j == 2 * (n - i - 1) - 2:
            print('*', end=' ')
        else:
            print(' ', end=' ')
    print()
print()
for i in range(1, n + 1):
    for j in range(n * 2 - i * 2):
        print(' ', end='')
    for k in range(2 * i - 1):
        print('*', end=' ')
    print()
for i in range(n - 1):
    for j in range(i + 1):
        print(' ', end=' ')
    for j in range(2 * (n - i - 1) - 1):
        if j == 0 or j == 2 * (n - i - 1) - 2 or j == (n - i - 1) - 1:
            print('*', end=' ')
        else:
            print(' ', end=' ')
    print()




