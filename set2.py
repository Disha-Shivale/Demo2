#Check lenght of set
names = {"Item 1", "Item 2", "Item 3", "Item 4"}
print("Values count in set are ", len(names))
print()

#Union() method in set
i = {"Item 1", "Item 2", "Item 3"}
j = {"Item 4", "Item 5", "Item 6"}
values = i.union(j)
print(values)
print()

#Delete Set
print(names)
print()
del names
print(names)