# (condition) ? x : y
# 1- if-else --> x if condition else y
x, y = 4, 2

if x < y:
    min_ = x
else:
    min_ = y

m = x if x < y else y
# print('min: ', x) if x < y else print('min: ', y)

# 1.2- elif --> x if condition1 else y if condition2 else z
#               (      if      ) (        elif     ) ( else )
m = x if x < y else -10 if x == 5 else y

# 2- tuple / list --> (y, x)[condition]

min_ = (y, x)[x < y]

# 3- dictionary --> {False: y, True: x}[condition]

min_ = {False: y, True: x}[x < y]


# 4- lambda --> (lambda: y, lamda: x)[condition]()

min_ = (lambda: y, lambda: x)[x < y]()

# 5- logical operator --> condition and x or y

# print(x and y)  # return x if x is False
# print(x or y)   # return x if x is True

x, y = 1, 4
min_ = x < y and x or y
# True and x or y
# x or y
# y

x, y = 4, 6
min_ = x < y and x or y
# False and x or y
# False or y
# y

min_ = (x < y and [x] or [y])[0]
#   -----------------------------------------------------*********-----------------------------------------------------

