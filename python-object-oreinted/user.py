class User:
    def __init__(self, name="", phone="---"):
        self.user_id = id(self)
        self.name = name
        self.__phone = phone

    def set_phone(self, phone):
        if len(phone) == 11 and phone.isnumeric:
            self.__phone = phone

    def get_phone(self):
        return self.__phone


class Person:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    def __repr__(self):
        return f"{self.__class__.__name__} (' {self.first_name}', '{self.last_name}', '{self.age}')"


person1 = Person('ali', 'mohammadi', 24)
print(str(person1))
print(repr(person1))






