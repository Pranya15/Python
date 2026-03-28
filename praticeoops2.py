#circle
# class Circle:
#     def __init__(self, radius):
#         self.radius = radius

#     def area(self):
#         return (22/7) * self.radius ** 2
    
#     def perimeter(self):
#         return 2 * (22/7) * self.radius


# c1 = Circle(21)
# print(c1.area())
# print(c1.perimeter())




#empolyee
# class Empolyee:
#     def __init__(self, role, dept, salary):
#         self.role = role
#         self.dept = dept
#         self.salary = salary

#     def showdetails(self):
#         print("role=",self.role)
#         print("dept=",self.dept)
#         print("salary=",self.salary)

# class Engineer(Empolyee):
#     def __init__(self, name , age):
#         self.name = name
#         self.age = age

#         super().__init__("Engineer","IT","75000")

# e1 = Empolyee("accountant","Finance","30000")
# engg1= Engineer("Pranya",22)
# engg1.showdetails()



#order
class Order:
    def __init__(self, item, price):
        self.item = item
        self.price = price

    def __gt__(self, odr2):
        return self.price > odr2.price

odr1 = Order("chips",20)
odr2 = Order("tea",10)

print(odr1 > odr2)