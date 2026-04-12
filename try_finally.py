try:
    a = int(input("Hey, Enter a number:"))
    print(a)
except Exception as e:
    print(e)

#works with both vaild and invalid , it is  used in fuction 
finally:
    print("Hey, I am inside of finally") 