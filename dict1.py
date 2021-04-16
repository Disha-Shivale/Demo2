#Print Keys & values of dictionaries
i = {
'name': 'Felix',
'city': 'Pune',
'since': '10 years'
}
print(i)
print()

#Access Items
print(i['name'])
print(i['city'])
print()

#Get() Method
print(i.get('name'))
print(i.get('since'))
print()

#Change value
i['since'] = "20 Years"
print(i)
print()