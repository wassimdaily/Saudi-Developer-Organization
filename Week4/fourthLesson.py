# check of the kyes or value are there or not.

data = {
'name': 'waseem',
'email': 'businesswassim@gmail.com'
}

# check by call the value of key name
if 'waseem' in data['name']:
	print('yes')
else:
	print('no')
# check by call name of the key

if 'name' in data:
	print('key is exist')
else:
	print('no')

# to calculate the length of the dictionary by using len() function


print("The number of the keys in dictionary 'data' are {}").format(len(data))

"""Add phone key with value to the data dictionary.
 If the key is not exist then the compiler make new one to the dictionary. 
"""

data['phone_number'] = '00966534551890'

print(', '.join([str(x) for x in data]))


# pop or remove item in dictionary and exist by using pop() & popitem().

data.pop('phone_number') # delete specific key & value.
data.popitem() # delete random key & value

# delete all dictionary form the memory 
data.clear() # clear all elements of the dictionary
del data
