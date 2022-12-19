#task_1
number_1 = int(input("Enter operator: "))
number_2 = int(input("Enter operator: "))
operand = input("Enter operands (+,-,*,/,**): ")
if operand == "/" and number_2 == 0:
    print("You can't divide by zero!")
elif operand == "+":
    print(number_1+number_2)
elif operand == "-":
    print (number_1-number_2)
elif operand == "*":
    print(number_1*number_2)
elif operand == "/":
    print(number_1/number_2)
elif operand != "+" or operand != "*" or operand != "-" or operand != "/":
    print("Invalid operand")
print()
#task_2
number = int(input("Enter an integer: "))
i = 1
while i**2 <= number:
    print(i**2, end=' ')
    i += 1
print()
#task_3
number = int(input("Enter number: "))
if number == 1:
    print("Not a prime number")
else:
    for i in range(2, number):
        if number % i == 0:
            print("Not a prime number")
            break
    else:
        print("Prime number")
# task_4
mushrooms = int(input("Enter number of mushrooms: "))
if mushrooms == 0 or (10 <= mushrooms % 100 <= 20):
    print(f'Маша нашла в лесу {mushrooms} грибов')
elif mushrooms % 10>= 2 and mushrooms%10 <= 4:
    print(f'Маша нашла в лесу {mushrooms} гриба')
elif mushrooms % 10 == 1:
    print(f'Маша нашла в лесу {mushrooms} гриб')
else:
    print(f'Маша нашла в лесу {mushrooms} грибов')
