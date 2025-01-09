a, b = 4, 6
# print(f'{a}, {b}')

a = a + b
b = a - b
a = a - b
# print(f'{a}, {b}')

a, b = b, a
# print(f'{a}, {b}')

#  ______________________

a, b, c = 1, 2, 3

a, b, *c = 4, 5, 6, 7, 8, 9

# ________________________

def training_warlus():
    answer = input('Do you want to continue? ')
    while 'y' in answer.lower():
        x = int(input("Enter a number: "))
        print(x ** 2)
        answer = input('Do you want to continue? ')


def training_warlus_2():
    while 'y' in (answer := input('Do you eant continue? ').lower()):
        x = int(input('Enter a number: '))
        print(x ** 2)


# ________________________


