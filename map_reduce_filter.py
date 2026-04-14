from functools  import reduce

#map eg
l = [1, 2, 3, 4, 5]

square = lambda x : x*x

sqList = map(square, 1)
print(list(sqList ))

#filter eg
def even(n):
    if(n%2==0):
        return True
    return False

onlyEven = filter(even, 1)
print(list(onlyEven))

#reduce eg
def sum(a,b):
    return a+b
print(reduce(sum, l))