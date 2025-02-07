from pprint import pprint


class Rectangle:
    """
    Create Rectangle Object and Calculate its perimeter and environment
    """
    all_rectangles: list["Rectangle"] = []

    def __init__(self, width: float, length: float, height: float = 0) -> None:
        self.width = width
        self.length = length
        self.height = height
        Rectangle.all_rectangles.append(self)

    def __str__(self) -> str:
        return f'Rectangle number of {Rectangle.all_rectangles.index(self) + 1}: width: {self.width}, length: {self.length}'

    def __repr__(self) -> str:
        return f'{self.__class__.__name__}({self.width!r}, {self.length!r}, {self.height!r})'

    def display(self) -> None:
        """
        Show info about Rectangle
        :return:
        """
        pprint(self.__str__())

    def perimeter(self) -> float:
        """
        Calculate perimeter of Rectangle
        :return: flout -> perimeter
        """
        perimeter = (self.width + self.length) * 2
        return perimeter

    def environment(self) -> float:
        """
        Calculate environment of Rectangle
        :return: flout -> environment
        """
        environment = (self.width * self.length)
        return environment

    def help_perimeter(self) -> None:
        """
        It shows and explains the steps of perimeter calculation
        :return: None -> print in Method
        """
        print(f'Rectangle Perimeter: \n\t\tperimeter = 2 * (width + length)')
        print(f'\nIn your Rectangle: \n\t\t_ {self.perimeter()} _ = 2 * ({self.width} + {self.length})')

    def help_environment(self) -> None:
        """
        It shows and explains the steps of environment calculation
        :return: None -> print in Method
        """
        print(f'Rectangle environment: \n\t\tenvironment = width * length')
        print(f'In your Rectangle: \n\t\t_ {self.environment()} _ = {self.width} * {self.length}')


class Car:
    """
    information of Cars --> brand, model, year
    """
    all_car: list["Car"] = []

    def __init__(self, name: str, brand: str, model: str, age: str):
        self.name = name
        self.brand = brand
        self.model = model
        self.age = age
        Car.all_car.append(self)

    def __str__(self) -> str:
        return f'{self.name}/ Year {self.age}/ {self.brand}'

    def __repr__(self) -> str:
        return f'{self.__class__.__name__}({self.name!r}, {self.brand!r}, {self.model!r}, {self.age!r})'

    def display(self) -> str:
        """
        Show information of Car
        :return:
        """
        return (f"Car information: \n name: {self.name}\n company: {self.brand}\n model: {self.model}\n"
                f" year: {self.age}")


class Student:
    courses_offered: list[tuple] = []
    # Course_units
    base_student_id = 402784100
    all_student: list["Student"] = []

    def __init__(self, first_name: str, last_name: str, age: int, major: str, phone: str):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.student_id = Student.base_student_id + 1
        Student.base_student_id += 1
        self.major = major
        self.phone = phone

        self.email = ''
        self.address = ''
        self.scores = {}
        self.gpa = 0
        self.status = 'Waiting for information to be completed'
        self.courses = []
        self.credits_units = 0
        Student.all_student.append(self)

    def __str__(self) -> str:
        return f'Student: {self.first_name} {self.last_name}\tStudent: {self.student_id}'

    def __repr__(self) -> str:
        return (f'{self.__class__.__name__}({self.first_name!r}, {self.last_name!r}, {self.age!r}, {self.major!r}, '
                f'{self.phone})')

    def add_courses_offered(self) -> None:
        """
        add list of student courses
        :get str -> course_1, unit/course_2, unit
        :return:
        """
        print('Enter a list of courses with units.')
        courses = list(input('course_1, unit/course_2, unit: ').split('/'))
        courses = list(map(lambda x: tuple(x.split(', ')), courses))
        Student.courses_offered.extend(courses)

    def show_all_info(self) -> None:
        print(f'first_name: {self.first_name}\nlast_name: {self.last_name}\nage: {self.age}\nstudent_id: {self.student_id}'
              f'\nmajor: {self.major}\nphone: {self.phone}\nemail: {self.email}\naddress: {self.address}\nscores: '
              f' {self.scores}\n GPA: {self.gpa}\nstatus: {self.status}\ncourses: {self.courses}\ncredits_units: '
              f' {self.credits_units}\n')

    def edit_info(self) -> None:
        while True:
            print('Edit info\n\nChoice a option:\n\t\t1.show info\n\t\t2.name and age\n\t\t3.major\n\t\t4.email ans '
                  'phone\n\t\t4.address\n\t\t5.status')
            print('_' * 40)
            ch = input('enter a number:')
            if ch == '1':
                self.show_all_info()
            elif ch == '2':
                print(f'first name: {self.first_name}\nlast name: {self.last_name}\nage: {self.age}')
                first_name = input('new first name: ')
                last_name = input('new last name: ')
                age = input('new age: ')

                if first_name:
                    self.first_name = first_name
                if last_name:
                    self.last_name = last_name
                if age:
                    self.age = age
            elif ch == '3':
                print(f'major: {self.major}')
                major = input('new major: ')
                if major:
                    self.major = major
            elif ch == '4':
                print(f'email: {self.email}\nphone: {self.phone}')
                email_ = input(f'new email: ')
                phone = input('new phone: ')
                if email_:
                    self.email = email_
                if phone:
                    self.phone = phone
            elif ch == '4':
                print(f'address: {self.address}')
                address = input('new address: ')
                if address:
                    self.address = address
            elif ch == '5':
                if self.status != 'Waiting for information to be completed':
                    print('choice a status. \n\t\t1.Active\n\t\t2.Deactivate\n\t\t3.Graduated\n\t\t4.Conditional')
                    ch = input('enter a number')
                    if ch == '1':
                        self.status = 'Active'
                    elif ch == '2':
                        self.status = 'Deactivate'
                    elif ch == '3':
                        self.status = 'Graduated'
                    elif ch == '4':
                        self.status = 'Conditional'
                    else:
                        print('your choice is invalid!!')
                else:
                    print(f'your status: {self.status}\n first complete your information!!')
            else:
                break

    def set_scores(self):
        while True:
            print(40 * '_')
            n = input('1.To Continue 2.Exit')
            if n == '2':
                break
            print(f'choice a course to set score: ')
            for index, course in enumerate(self.courses):
                print(f'{index + 1}.{course}', end=' _ ')
            ch = int(input('enter a number: '))
            score = int(input(f'new score of {self.courses[ch - 1]}: '))
            if 0 <= score <= 20:
                self.scores[self.courses[ch - 1]] = score
            else:
                print('Invalid Score !!')

    def get_pga(self):
        pass

    def display(self):
        self.__str__()

    def get_units(self):
        print(f'Course units obtained: {self.credits_units}\nLessons learned: ', self.courses)

    def add_course(self):
        pass

    def delete_course(self):
        pass

    def update_status(self):
        pass

    def check_graduation_status(self):
        pass

    def get_course_list(self):
        pass







def main():
    pass


if __name__ == '__main__':
    main()
