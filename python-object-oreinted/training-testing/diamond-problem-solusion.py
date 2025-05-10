from pprint import pprint


class BaseClass:
    num_base_calls = 0

    def __init__(self, a, b, **kwargs):
        self.a = a
        self.b = b

    def call_me(self):
        print('calling method on BaseClass!')
        self.num_base_calls += 1


class LeftSubClass(BaseClass):
    num_left_calls = 0

    def __init__(self, c, **kwargs):
        super().__init__(**kwargs)
        self.c = c

    def call_me(self):
        # BaseClass.call_me(self)
        super().call_me()
        print("calling method on LeftSubClass!")
        self.num_left_calls += 1


class RightSubClass(BaseClass):
    num_right_class = 0

    def __init__(self, d, e, f, **kwargs):
        super().__init__(**kwargs)
        self.d = d
        self.e = e
        self.f = f

    def call_me(self):
        # BaseClass.call_me(self)
        super().call_me()
        print('calling method on RightSubClass!')
        self.num_right_class += 1


class SubClass(LeftSubClass, RightSubClass):
    num_sub_class = 0

    def __init__(self, g, **kwargs):
        super().__init__(**kwargs)
        self.g = g

    def call_me(self):
        # LeftSubClass.call_me(self)
        # RightSubClass.call_me(self)
        super().call_me()
        print('calling method on SubClass!')
        self.num_sub_class += 1


s = SubClass(a=1, b=2, c=3, d=4, e=5, f=6, g=7)

pprint([s.a, s.b, s.c, s.d, s.e, s.f, s.g])

# super یک الگوریتمی داره به نام MRO که از این مشکل دوبار صدا زدن بیس جلوگیری میکنه
# اما دیگه ترتیب ممکنه به شکل دیگری باشه
# print(SubClass.__mro__)  با این میشه ترتیبش رو دید
# subclass وقتی داره مقدار دهی میشه باید همه کلاس های پدر را هم مقدار دهی کند.
# برای مقدار دهی چندگانه ترتیب خیلی مهمه و باید ترتیب MRO را بدانیم
#     def __init__(self, g, *args):
#         super().__init__(*args)
#         self.g = g
#         ---
#
#         def __init__(self, d, e, f, *args):
#             super().__init__(*args)
#             self.d = d
#             self.e = e
#             self.f = f
#         ---
#         pprint([s.a, s.b, s.c, s.d, s.e, s.f, s.g])
# **kwargs کهی و ولیو هست و دیگه ترتیب کمرنگ تر میشه و روی کلید ها مقدار میده
# pprint([a=s.a, b=s.b, c=s.c, d=s.d, e=s.e, f=s.f, g=s.g])
