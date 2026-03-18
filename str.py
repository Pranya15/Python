str1 = "this is a string...\nwe are creating it in python.."
str2 = "\nI'm Pranya Patel"
print(str1)
print(str1+str2) #concatination
print(len(str2)) #length
len2 = len(str1)
print(len2)

#indexing
str = "learning python"
ch = str[0]
print(ch)
print(str[8])

#slicing 
print(str[0:8])
print(str[5:len(str)])
print(str[5:])
print(str[:5 ])


str = "i am learning python"
print(str.endswith("hon"))
print(str.capitalize())

str= str.capitalize()
print(str)

#print(str.replace("o","a"))

print(str.find("o"))
print(str.find("Q"))

print(str.count("n"))