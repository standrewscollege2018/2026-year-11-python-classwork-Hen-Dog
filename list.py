'''the making of lists and the different functions that can be used with them'''

# we use square brackets to make a list
# DO NOT USE CAPITALS!!!

names = ["Zac", "Cayden", "Henry"]

# print entire list
# this is useful for debugging "print(names)"

print (names [0])

# using negative index counts backwards from the end
# -1 is the last item, -2 is the second to last item and so on

print(names[-1])

# we can use len() to find the length of the list

length = (len(names))

# print(len(names[0])) will print the length of the item on the list

print(len(names[0]))

# to change an item on the list we can overwrite it by setting a new value -
# in the postion of the list

names[0] = "Zesty Zac"
print(names)

# you can insert a new item into the list using the insert() function

names.insert(1, "Spencer king of bowlcuts")
print(names)

# most common method to add an item to the end of the list is using append()

names.append("Cayden is Cayden")
print(names)

# making it look nice
for name in names:
    print(name)

# this will loop through the list and print each item on a new line

# other method is displaying list in a numbered list
for i in range(len(names)):
    print(f"{i+1}. {names[i]}")

# i + 1 is used to make the numbering start at 1 instead of 0


