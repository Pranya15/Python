# class Student:
#     name = "Pranya Patel"

# sl = Student()
# print(s1.name)


# class Car:
#     color = "blue"

# c1 = Car()
# print(c1.color)


class Student:
    
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
        print("adding new student")

    def welcome(self):
        print("Welcome student,", self.name)


s1 = Student("karan", 78)
print(s1.name, s1.marks)
s1.welcome()

s2 = Student("arjun", 99)
print(s2.name, s2.marks)
s2.welcome()

