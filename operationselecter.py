a = float(input('Enter a number: '))
b = float(input('Enter another number: '))

Addition = 0
Subtraction = 0
Multiplication = 0
Divison = 0

print("\nChoose your operation")
print('1) Addition (+)')
print('2) Subtraction (-)')
print('3) Multiplication (*)')
print('4) Division(/)')

answer = int(input('Enter numbers from (1-4): ' ))

if answer == 1:
    print(a + b)

elif answer == 2:
    print(a - b)

elif answer == 3:
    print(a * b)

elif answer == 4:
    print(a / b)

else:
    print('Wrong input')


