#  info = {
#     "key" : "value",
#     "name" : "pranya",
#     "learning" : "coding",
#     "age" : 35,
#     "is_adult" : True,
#     "marks" : 94.4
#  }
#  print(type(info))


student = {
    "name" : "rahul kumar",
    "sub" : {
        "phy" : 55,
        "chem" : 98,
        "maths" : 70
    }
}
#nested dict

print(student)
print(student["sub"])
print(student["sub"]["chem"])


student.update({"city" : "Delhi", "age" : 18})
print(student)