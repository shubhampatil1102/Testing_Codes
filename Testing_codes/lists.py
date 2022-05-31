
friends = ["mike","kevin","PT","noname"]

print(friends[2])

#  List functions

# Adding two lists

lucky_numbers = [4,5,6,7]
name_friends = ["male","male","male","female","gender","trans"]

name_friends.extend(lucky_numbers)
print(name_friends)

#  adding name to the existing list using APPEND

name_friends.append("noname")
print(name_friends)

#  Adding name to the list using INSERT

name_friends.insert(0,"thisisfirst")
print(name_friends)

# To remove the name from list using REMOVE

name_friends.remove("gender")
print(name_friends)

# using CLEAR function we can remove the whole array list

# name_friends.clear()

# Counting name from the list

print(name_friends.count("male"))

# sorting array

friends.sort()
print(friends)

# 