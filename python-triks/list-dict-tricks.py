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

# max and min in list

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
list_4 = list_4 + final_list


final_list = list_4.copy()
final_list.sort()
final_list = final_list[-n:]

# import heapq
# final_list = heapq.nlargest(3, list_4)
# final_list = heapq.nsmallest(3, list_4)

# string to dar to --> real list

# import json
# str_list = input('str: ')
# str_list = json.loads(str_list)
#
# import ast
# str_list_2 = input('str: ')
# str_list_2 = ast.literal_eval(str_list_2)


# sorted Dictionary with value

dict_ = {"a": 4, "b": 9, "c": 7, "d": 8, "e": 0}

sorted_value = sorted(dict_.values())
sorted_dict = {}

for i in sorted_value:
    for k in dict_.keys():
        if dict_[k] == i:
            sorted_dict[k] = dict_[k]
            break

# from operator import itemgetter
# sorted_dict_4 = dict(sorted(dict_.items(), key=itemgetter(1)))

sorted_dict_2 = {k: v for k, v in sorted(dict_.items(), key=lambda item: item[1])}

sorted_dict_3 = {k: dict_[k] for k in sorted(dict_, key=dict_.get)}


# round method
r1 = round(18456.7564)
r2 = round(18456.7564, 2)
r3 = round(18456.7564, -2)
r4 = round(18456.7564, -4)

# پیدا کردن یک کلمه و نشون دادن کلمات قبل و بعد

text = '''
    Einblick reimagines the modern data science workflow in a collaborative data science canvas,
    rather than a linear notebook. Working in a canvas environment offers many advantages including
    live collaboration, an expansive visual interface, and a progressive computation engine.
    In this article, we’ll highlight one of the key ways we’re saving data scientists time–our
    operators. We’ll go through a couple of our core operators, why Python is such a crucial
    part of our software solution, and how we augmented our offerings with a user operator
    interface. The latter allows users to customize and use their own operators, which can
    be used in any Einblick canvas, and shared with other Einblick users.
'''

search = lambda tex, q: tex[tex.find(q) - 30: tex.find(q) + 30] if q in tex else -1
search(text, 'notebook')

# بررسی یکسان بودن همه اعضای یک لیست
my_list = [5] * 10
def all_element_same(lst):
    if not lst:
        return True
    first_element = lst[0]
    for element in lst:
        if first_element != element:
            return False
    return True


def all_element_same_2(lst):
    return len(set(lst)) == 1


def all_element_same_3(lst):
    return all(x == lst[0] for x in lst)


def all_element_same_4(lst):
    return True if lst.count(lst[0]) == len(lst) else False


# list comprehension به جای filter و map

lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]
squares = [i ** 2 for i in lst]
squares_map = list(map(lambda x: x ** 2, lst))

squares_odd = [i ** 2 for i in lst if i % 2 != 0]
squares_odd_map_filter = list(map(lambda x: x ** 2, filter(lambda x: x % 2 != 0, lst)))

squares_dict = {i: i ** 2 for i in lst if i % 2 != 0}
squares_dict_map_filter = dict(map(lambda x: (x, x ** 2), filter(lambda x: x % 2 != 0, lst)))


# مقایسه دو لیست نامرتب بدون تکرار

l1 = [1, 2, 3, 4]
l2 = [2, 1, 3, 4]

a = sorted(l1) == sorted(l2)
b = set(l1) == set(l2)  # تکرار ها را نادیده میگیره

# from collections import Counter
# c = Counter(l1) == Counter(l2)
