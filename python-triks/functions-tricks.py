from collections import namedtuple

User_Info = namedtuple('UserInfo', 'first_name last_name age job city')


def get_user_info():
    return User_Info(first_name='Ali', last_name='Mohammadi', age=29, job='Programmer', city='Isfahan')


user_info = get_user_info()

print(user_info.first_name, ':', user_info.last_name)

# ________________


class UserInfo2:
    def __init__(self, first_name, last_name, age, job, city):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.job = job
        self.city = city


def get_user_info_2():
    return UserInfo2(first_name='ali', last_name='mohammadi', age=26, job='programmer', city='isfahan')


user_info_2 = get_user_info_2()
print(user_info_2.first_name, ':', user_info_2.last_name)