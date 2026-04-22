def divisible5(n):
    if(n%5 == 0):
        return True
    return False
a= [1,2,334567,6543,5678,23456789,987654,77,18,5]

f= list(filter(divisible5, a))
print(f)