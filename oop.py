class Person(object):
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def introduce(self):
        print(
            f"Hello, my name is {self.name}, I am {self.age} years old and my gender is {self.gender}"
        )


person1 = Person("Karume", 20, "Male")
person1.introduce()
