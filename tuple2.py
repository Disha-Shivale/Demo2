#Change tuple value
names = ("Item 1", "Item 2", "Item 3", "Item 4", "Item 5", "Item 6")
i = list(names)
i[0] = "Felix";
print(i)

#Check tuple values
if "Item 1" in names:
    print()
    print("Value is available")
else:
    print()
    print("Value is not available")

#Tuple lenght
print()
print("Value is ", len(names))
print()

#Merge two tuples
names = ("Item 1", "Item 2", "Item 3")
names1 = ("Item 4", "Item 5", "Item 6")
print(names + names1)
print()

#Delete tuple
del names
print(names)


