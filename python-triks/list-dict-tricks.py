import itertools

#  ترکیب دو لیست
names = ['reza', 'ali', 'zeinab', 'neda']
ages = [26, 20, 25, 24]
dict_1 = {}
for i in range(min(len(names), len(ages))):
    dict_1[names[i]] = ages[i]

dict_2 = dict(zip(names, ages))

# تبدیل لیست های تو در تو به لیست مسطح

list_x = [[1, 2, 3, 4], (5, 6, 7), "890", "ali mohammadi", {1, 2, 3, 4}]
x = []
for iterable in list_x:
    for item in iterable:
        x.append(item)

x_2 = list(itertools.chain.from_iterable(list_x))

# جا به جایی کلیدها و مقادیر دیکشنری

dict_3 = {'ali': 24, 'reza': 23, 'neda': 19}
inverse_dict = {}
for key, value in dict_3.items():
    inverse_dict[value] = key

inverse_dict_2 = {value: key for key, value in dict_3.items()}

inverse_dict_3 = dict((value, key) for key, value in dict_3.items())

inverse_dict_4 = dict(map(reversed, dict_3.items()))

# جمع کردن چند دیکشنری

dict_4 = {'a': 1, 'b': 2}
dict_5 = {'c': 3, 'd': 4}
dict_6 = {'e': 5}

dict_4_5 = dict_4.copy()
dict_4_5.update(dict_5)

dict_4_5_6 = dict_4 | dict_5 | dict_6

dict_4_5_6 = {**dict_4, **dict_5, **dict_6}

# مقدار دهی و ساخت مانریکس

matrix = []
for i in range(4):
    m = []
    for j in range(4):
        m.append(0)
    matrix.append(m)

matrix_2 = [[0] * 4, [0] * 4, [0] * 4, [0] * 4]

matrix_3 = [[0 for j in range(4)] for i in range(4)]

# تفاوت دو لیست

list_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
list_2 = [1, 2, 4, 5, 6, 7, 9]

list_diff = []
for i in list_1:
    if i not in list_2:
        list_diff.append(i)

list_diff_2 = list(set(list_1).symmetric_difference(set(list_2)))

# چرخش لیست

list_3 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# list[n:] + list[:n]
list_ = list_3[3:] + list_3[:3]

#

list_4 = [1, 2, 12, 9, 8, 7, 6]
final_list = []
n = 3
for i in range(0, n):
    # max_ = 0
    max_ = float("-inf")
    for j in list_4:
        if j > max_:
            max_ = j
    list_4.remove(max_)
    final_list.append(max_)


















