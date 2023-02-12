class Person():
    def __init__(self, name, age):
        self.name = name
        self.age = age

people = {
        "Charlie": Person("Charles", 23),
        "James": Person("James", 45)
        }
print(people["James"].age)

