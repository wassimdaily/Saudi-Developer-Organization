# dictionary

jsonData = {
	'name': 'waseem',
	'email': 'businesswassim@gmail.com',
	'phone_number': '00966534551890',
	'twitter_account': 'wDayili',
	'telegram_account': 'vvvn1'
	}

# print all keys of the jsonData dictionary

print('All keys are:')
for x in jsonData:
	print(x)

print('All values of the kyes are:')
for y in jsonData:
	print(jsonData[y])


# change value of the key
jsonData['email'] = 'dayiliwaseem@gmail.com'
print(jsonData['email'])

# also you can use values() to call all values of the dictionary without for loop

print(jsonData.values())

# also you can use items() to call all items of the dictionary without for lo$

print(jsonData.items())



#print all items {key & value} by using for loop


for x in jsonData:
	print('key-> '+str(x)+' value-> '+str(jsonData[x]))
