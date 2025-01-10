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

li = [1, 2, 2, 3, 9, 7, 8, 3, 3, 8, 8, 8, 8]


def most_frequent(list):
    counter = 0
    element = list[0]
    for i in set(list):
        frequent = list.count(i)
        if frequent > counter:
            counter = frequent
            element = i
    return element


def most_frequent_2(list):
    print(max(set(list), key=li.count))


# ______________________________
from pprint import pprint


matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]  
]


def mat_(matrix_):
    transposed = []
    for i in range(len(matrix_[0])):
        transposed_row = []
        for row in matrix_:
            transposed_row.append(row[i])
        transposed.append(transposed_row)
    pprint(transposed, width=20)


def mat_2(matrix_):
    transposed = []
    for i in range(len(matrix_[0])):
        transposed_row = []
        transposed.append([row[i] for row in matrix_])
    pprint(transposed, width=20)


def mat_3(matrix_):
    transposed = [[row[i] for row in matrix_] for i in range(len(matrix_[0]))]
    pprint(transposed, width=20)


def mat_4(matrix_):
    pprint([list(i) for i in list(zip(*matrix_))], width=20)


#  __________________________



