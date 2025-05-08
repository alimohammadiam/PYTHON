class BaseClass:
    num_base_calls = 0

    def call_me(self):
        print('calling method on BaseClass!')
        self.num_base_calls += 1


class LeftSubClass(BaseClass):
    num_left_calls = 0

    def call_me(self):
        # BaseClass.call_me(self)
        super().call_me()
        print("calling method on LeftSubClass!")
        self.num_left_calls += 1


class RightSubClass(BaseClass):
    num_right_class = 0

    def call_me(self):
        # BaseClass.call_me(self)
        super().call_me()
        print('calling method on RightSubClass!')
        self.num_right_class += 1


class SubClass(LeftSubClass, RightSubClass):
    num_sub_class = 0

    def call_me(self):
        # LeftSubClass.call_me(self)
        # RightSubClass.call_me(self)
        super().call_me()
        print('calling method on SubClass!')
        self.num_sub_class += 1


# super یک الگوریتمی داره به نام MRO که از این مشکل دوبار صدا زدن بیس جلوگیری میکنه
# اما دیگه ترتیب ممکنه به شکل دیگری باشه
# print(SubClass.__mro__)  با این میشه ترتیبش رو دید

s = SubClass()
s.call_me()
print(s.num_sub_class, s.num_left_calls, s.num_right_class, s.num_base_calls)