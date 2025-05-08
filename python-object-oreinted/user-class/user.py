from pprint import pprint


class UserList(list["User"]):
    def search(self, user_name: str) -> list["User"]:
        matching_users: list["User"] = []
        for user in self:
            if user_name in user.user_name:
                matching_users.append(user)
        return matching_users

    def append(self, obj) -> None:
        if not isinstance(obj, User):
            raise TypeError('This List only accepts User ')
        return super().append(obj)


class User:
    all_users: list["User"] = UserList()

    def __init__(self, user_name: str, email: str, password: str, **kwargs) -> None:
        self.user_name = user_name
        self.email = email
        self.password = password
        User.all_users.append(self)

    def __repr__(self):
        return f'{self.__class__.__name__}({self.user_name!r}, {self.email!r}, ' \
               f'{self.password!r})'

    def __str__(self):
        return f'{self.user_name}'


class Seller(User):
    def __init__(self, shaba: str, **kwargs):
        super().__init__(**kwargs)
        self.shaba = shaba

    def __repr__(self):
        return f'{self.__class__.__name__}({self.user_name!r}, {self.email!r}, ' \
               f'{self.password!r}, {self.shaba!r})'

    def order(self, order: "Order") -> None:
        print(f'{self.user_name}, From your product, {order} was sold!')


class Bauer(User):
    def __init__(self, phone: str, **kwargs) -> None:
        super().__init__(**kwargs)
        self.phone = phone

    def __repr__(self):
        return f'{self.__class__.__name__}({self.user_name!r}, {self.email!r}, ' \
               f'{self.password!r}, {self.phone!r})'


class SellerAndBauer(Seller, Bauer):
    def __init__(self, score, **kwargs):
        super().__init__(**kwargs)
        self.score = score

    def __repr__(self):
        return f'{self.__class__.__name__}({self.user_name!r}, {self.email!r}, ' \
               f'{self.password!r}, {self.phone!r}, {self.shaba}, {self.score})'


def main():
    s = Seller(shaba='6097997521609157', user_name='AliMohammadi', email='ali0182@gmail.com', password='123')
    b = Bauer(user_name='khoda', email='khoda@gmail.com', password='321', phone='09925126890')
    sb = SellerAndBauer(score='100', shaba='456', phone='0313131', user_name='aaa', email='bbb', password='333')
    pprint(User.all_users)


if __name__ == '__main__':
    main()
