# collection = {1,2,3,4,4}
# print(type(collection))
# print(collection)
# print(len(collection))

collection= {} # empty dict
collection = set() #empty set

# print(type(collection)) 

collection.add(1)
collection.add(2)
collection.add(1)
collection.add("hello")

collection.remove(2)

collection.clear()

print(collection)
print(len(collection))


set1 = {1,2,3}
set2 = {2,3,4}

print(set1.union(set2))
print(set1)
print(set2)
print(set1.intersection(set2))