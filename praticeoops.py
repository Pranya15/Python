class Student:
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks

    def get_avg(self):
        sum = 0
        for value in self.marks:
            sum += value
        print("hi,", self.name, "Your avg score is =", sum/3)
s1 = Student("Neha",[87,92,56])
s1.get_avg()