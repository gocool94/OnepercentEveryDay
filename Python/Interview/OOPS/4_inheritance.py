'''
- Design a class structure for a library system with `Person`, `Author`, and `Book` classes using inheritance.
'''


class Library:
    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age

    def display(self):
        print(f"name : {self.name} age: {self.age}")


class Person(Library):
    def __init__(self, name, age, Books_owned) -> None:
        super().__init__(name, age)
        self.Books_owned = Books_owned


class Author(Person):
    def __init__(self, name, age, Books_owned) -> None:
        super().__init__(name, age, Books_owned)
