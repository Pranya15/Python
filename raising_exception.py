a = int(input("Enter the first num:"))
b = int(input("Enter the second num:"))

if(b==0):
    raise ZeroDivisionError("Hey our program is not meant to divide numbers by zero")
else:
    print(f"The divison a/b is{a/b}")