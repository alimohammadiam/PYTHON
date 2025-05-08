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

    def __init__(self, user_name: str, email: str, password: str) -> None:
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
    def order(self, order: "Order") -> None:
        print(f'{self.user_name}, From your product, {order} was sold!')


class Bauer(User):
    def __init__(self, user_name: str, email: str, password: str, phone: str) -> None:
        super().__init__(user_name, email, password)
        self.phone = phone

    def __repr__(self):
        return f'{self.__class__.__name__}({self.user_name!r}, {self.email!r}, ' \
               f'{self.password!r}, {self.phone!r})'


def main():
    pass


if __name__ == '__main__':
    main()
