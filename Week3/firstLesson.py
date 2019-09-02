listNames = ['Waseem', 'Ahmed', 'Ali', 'Mohammed']
phoneNumbers = ['0534551890', '0555555555', '0507777777', '0559876543']
count = -1
for x in listNames:
	print('The phone number of: '+x+' is ')
	for y in phoneNumbers:
		count = count + 1
		print(phoneNumbers[count])
		break

# change some values

listNames[0] = 'Rawan'
print(listNames)
del phoneNumbers[3]
print(phoneNumbers)
del phoneNumbers
print(phoneNumbers)
del listNames
print(listNames)
