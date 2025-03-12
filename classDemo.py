class Person:
    name = 'Talha'
    age = 20
    def description(self):
        print(f"""My name is {self.name} and I am {self.age} years old""")
a = Person()
nameInput = input("Enter your name: ")
a.name = nameInput
ageInput = input("Enter your age: ")
a.age = ageInput
a.description()        