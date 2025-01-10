# A - % operator 

a = 0b1011010
b = 0xf9b

# print("Binary: %d\nhex: %d" % (a, b))

# 1- مشکل--> جا به جایی سخت متغییر ها 

# 2- مشکل--> تغییرات جزیی باعث پیچیدگی و ناخوانایی میشه

weights = [
    ('reza', 80),
    ('ali', 65.5),
    ('zeinab', 50.3),
    ('sagar', 74),
]

# for i, (name, weight) in enumerate(weights):
#     print("#%d: %-10s = %.1f K" % (i+1, name.title(), round(weight)))

# 3- مشکل --> تکرار بی مورد یک متغییر

name = 'reza'
formatted = "He is %s. %s is beautiful boy! i`m not hate %s ..." % (name.title(), name.title(), name.title())
# S1 --> Dictionary
key = 'reza'
value = 65.50
formatted = "name: %(key)-15s weight: %(value)d" % {'key': key, 'value': value}

formatted = "He is %(name)s. %(name)s is beautiful boy! i`m not hate %(name)s ..." % {'name': name.title()}

# 4- مشکل پر حرفی (زیاده نویسی)

# B - bild-in method  format() ----------------------

x = 1234800.478623
formatted = format(x, "^20,.2f")

formatted = 'name: {} weight: {}'.format(key, value)

formatted = 'name: *{0:^10}* weight: {1:.1f}'.format(key, value)

formatted = 'He is {0}. {0} is beautiful boy! i`m not hate {0} ...'.format(name.title())

# for i, (name, weight) in enumerate(weights):              #  ناخوانایی کد خنوز وجود دارد
#     print("#{}: {:<10} = {:.1f} K".format(i+1, name.title(), round(weight)))

# C - f String ( Solusion all proplems ) ----------------------------

# for i, (name,weight) in enumerate(weights):
#     formatted = f'#{i}: {name:>10}= {weight:.1f}'
#     print(formatted)

formatted = f'He is {name.title()}. {name.title()} is beautiful boy! i`m not hate {name.title()} ...'

# --------------

key = 'ali'
value = 85.58
c_dict = '%(key)-10s = %(value).2f' % {'key':key, 'value': value}
str_kw = '{key:<10} = {value:.2f}'.format(key=key, value=value)
str_args = '{:<10} = {:.2f}'.format(key, value)
c_tuple = '%-10s = %.2f' % (key, value)
f_string = f'{key: <10} = {value: .2f}'

# -------------------------------------------Reversed String------------------------------------------
# 1
s = 'Ali Mohammadi'

reversed_s = ''.join(reversed(s))

# 2
reversed_s_2 = ''
for i in s:
    reversed_s_2 = i + reversed_s_2

# 3
from functools import reduce

reversed_s_3 = (reduce(lambda x, y: y + x, s))

# 4
reversed_s_4 = bytearray(s, "utf-8")
reversed_s_4.reverse()
reversed_s_4 = str(reversed_s_4.decode("utf-8"))

# 5 slicing
reversed_s_5 = s[::-1]
