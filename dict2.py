#Loop with Dictionary
i = {
'name': 'Felix',
'city': 'Pune',
'since': '10 years'
}
for values in i:
    print(values)

#Fetch value
print()
for values in i:
    print(i[values])

#Fetch both keys & values
values = {
'name': 'Felix',
'city': 'Pune',
'since': '10 years'
}
print()
for i,j in values.items():
    print(i, j)

#Delete values
print()
del values
print(values)