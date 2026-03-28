#single

# class Car:
#     @staticmethod
#     def start():
#         print("car started..")

#     @staticmethod
#     def stop():
#         print("car stopped..")


# class ToyotaCar(Car):
#     def __init__(self, name):
#         self.name = name


# car1 = ToyotaCar("BMW")
# car2 = ToyotaCar("GWagon")

# print(car1.name)
# print(car2.name)
# print(car1.start())



#multilevel

# class Car:
#     @staticmethod
#     def start():
#         print("car started..")

#     @staticmethod
#     def stop():
#         print("car stopped..")


# class ToyotaCar(Car):
#     def __init__(self, brand):
#         self.name = brand

# class BMW(ToyotaCar):
#     def __init__(self, type):
#         self.name = type

# car1 = BMW("Petrol")
# car1.start()


#multiple
class A:
    varA= "WELCOME TO CLASS A"

class B:
    varA= "WELCOME TO CLASS B"

class C(A,B):
    varC= "WELCOME TO CLASS C"
 
c1 = C()
print(c1.varC)
print(c1.varB)
print(c1.varA)

 