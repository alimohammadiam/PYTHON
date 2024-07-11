
class User:
    all_users: list["User"] = []

    def __init__(self, user_name: str, email: str, password: str):
        self.user_name = user_name
        self.email = email
        self.password = password
        User.all_users.append(self)

    def __repr__(self):
        return f"{__class__.__name__}({self.user_name!r}, {self.email!r}, {self.password!r})"

    def __str__(self):
        return f"{self.user_name}"
