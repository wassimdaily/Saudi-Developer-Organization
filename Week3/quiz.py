employes = ['waseem', 'rawan', 'mohammed', 'abdullah', 'asem', 'hassan']
blackList = ['hassan', 'asme']

# get details of the employes names and count.

count = 0

for x in employes:
	count = count + 1
print('Number of employes are: ', str(count))

# search about employee.

name = 'waseem'

if name in employes:
	print(name, ' is employee and his number is ', str(employes.index(name)))
	
else:
	print('is not employee.')
	employes.append(name)

if name in blackList:
	print('the name is in black list.')
	employes.remove(name)
else:
	print('the employee is good not in black list.')

# delete the black list

blackList.clear()

# find specifc word

match = 'python' 
tuple = ('java', 'python', 'swift')

if match in tuple:
	print('yes ',match+' is exist and ' ,str(tuple.index(match)), 'is the index of the matched value')
else:
	print("We can't ", match, ' in the list.')
