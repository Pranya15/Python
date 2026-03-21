seq = range(5)
#print(range(5))

# print(seq[0])
# print(seq[1])
# print(seq[2])
# print(seq[3])

for i in seq:
    print(i)


for i in range(10): #range(stop)
    print(i)


for i in range(2, 10): #range(start, stop)
    print(i)


for i in range(2, 10, 2): #range(start, stop, step) 2, 4, 6
    print(i)


for i in range(2, 101, 2): #even no
    print(i)


# print 100 to 1
for i in range(100, 0, -1):
print(i)


#table
n= int(input("Enter a no:"))
for i in range(1,11):
    print(n*i)