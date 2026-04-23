from functools import reduce
l= [1, 2, 44, 78, 928, 27,40 ,687  ]

def greater(a,b):
    if(a>b):
        return a
    return b
print(reduce(greater, l))