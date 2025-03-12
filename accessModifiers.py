class Student:
    def __init__(self,a,n):
        self.__age = a
        self.__name = n

    def show(self):
        print(f"""I am {self.__name} and I am {self.__age} years old.""")

x = Student(20,"Talha")
print(x._Student__age)