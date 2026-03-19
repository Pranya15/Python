# movies = []
# mov1 = input("Enter 1st fav movie :")
# mov2 = input("Enter 2nd fav movie :")
# mov3 = input("Enter 3rd fav movie :")

# movies.append(mov1)
# movies.append(mov2)
# movies.append(mov3)

# print(movies)

# movies = []
# movies.append(input("Enter 1st fav movie :"))
# mov = input("Enter 2nd fav movie :")
# movies.append(mov)
# mov = input("Enter 3rd fav movie :")
# movies.append(mov)

# print(movies)



#palindrome
list1 = [1,2,1]
list2 = [1,2,3]

copy_list1 = list1.copy()
copy_list1.reverse()

if(copy_list1 == list1):
    print('palindrome')
else:
    print("not palindrome")

    copy_list2 = list2.copy()
copy_list2.reverse()

if(copy_list2 == list2):
    print('palindrome')
else:
    print("not palindrome")