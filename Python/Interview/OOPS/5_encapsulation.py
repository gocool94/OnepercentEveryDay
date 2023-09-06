'''
- Implement a `Student` class with private attributes for name, age, and grade. Provide methods to access and modify these attributes.
'''


class Student:
    def __init__(self, name, age, grade) -> None:
        self.__name = name
        self.__age = age
        self.__grade = grade

    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age

    def get_grade(self):
        return self.__grade

    def set_name(self, name):
        self.__name = name

    def set_age(self, age):
        self.__age = age

    def set_grade(self, grade):
        self.__grade = grade


gokul = Student("Gokul", 26, "b")

gokul.set_name("happy")
print(gokul.get_name())
