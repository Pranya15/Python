# class Student:
#     def __init__(self, phy, chem , math):
#         self.phy = phy
#         self.chem = chem
#         self.math = math
#     #     self.percentage = str((self.phy + self.chem + self.math)/3) + "%"
#     # def calcPercentage(self):
#     #     self.percentage = str((self.phy + self.chem + self.math)/3) + "%"
  
#     @property
#     def percentage(self):
#         return str((self.phy + self.chem + self.math)/3) + "%"
  

# stu1 = Student(88,98,83)  
# print(stu1.percentage)    
# stu1.phy = 87
# print(stu1.percentage) 


 

class Complex:
    def __init__(self, real, img):
        self.real = real
        self.img = img


    def showNumber(self):
        print(self.real,"i +",self.img,"j")

    def add(self, num2):
        newReal = self.real + num2.real
        newImg = self.img + num2.img
        return Complex(newReal. newImg)

num1 = Complex(1,3)
num1.showNumber()


num2 = Complex(8,3)
num2.showNumber()


num3 = num1.add(num3)
num3.showNumber()




