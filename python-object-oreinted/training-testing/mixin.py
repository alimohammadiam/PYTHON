class PrintInfoMixin:
    def print_info(self):
        print(f'class: {self.__class__.__name__}\nAttribute:')
        for attr, value in self.__dict__.items():
            print(f'\t{attr}: {value}')


class MathOperationsMixin:
    def addition(self):
        return self.x + self.y

    def subtraction(self):
        return self.x - self.y

    def multiplication(self):
        return self.x * self.y

    def division(self):
        return self.x / self.y


class LoggingMixin:
    """Mixin برای اضافه کردن قابلیت لاگ کردن به هر کلاسی"""

    def log(self, message):
        class_name = self.__class__.__name__
        print(f"[LOG] {class_name}: {message}")

    def log_error(self, error_message):
        self.log(f"ERROR: {error_message}")


class Numbers(MathOperationsMixin):
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Vehicle:
    def __init__(self, color, weight, max_speed):
        self.color = color
        self.weight = weight
        self.max_speed = max_speed


class Car(Vehicle, PrintInfoMixin):
    def __init__(self, color, weight, max_speed, brand, fuel_type):
        super().__init__(color, weight, max_speed)
        self.brand = brand
        self.fuel_type = fuel_type
        self.current_speed = 0


# car = Car('red', '2Ton', 200, 'Kia-Optima', 'benzin')
# car.print_info()


# adad = Numbers(10, 2)
# print(adad.addition())
# print(adad.division())
# print(adad.subtraction())
# print(adad.multiplication())