# set of names , we have four names.
setOfNames = {'waseem', 'ahmed', 'ali', 'dayili'}

# by using len() function to calculate the number of items seted in the set
print('we have ' + str(len(setOfNames)) +' names are there.')

# there are two function to remove elemen in set 'remove() & discard()'

print('Names: ' + str(setOfNames))

# remove element by using discard()

setOfNames.discard('dayili')
print('Names: ' + str(setOfNames))

# pop() function used to remove last element of the set like a stack
setOfNames.pop()
print('Names: ' + str(setOfNames))

# to clear all elements of the set one same time by using clear() function
setOfNames.clear()
if setOfNames == set([]): # set([]) mean null , no elements are there
	print('the set is empty.')
else:
	print('there are elements.'+str(setOfNames))


# delete the set form the memory 'RAM - > Random access memory using for saved all instrctions of the computer.'

del setOfNames

# try call the set name after delete it.

try:

	print(setOfNames) # the error becaue we're delete it from the memory by using del() function in set.

# craete set of elements by using set() Constructor is main function of the set class
except:
	setOfNamesAgain = set(('waseem', 'ahmed', 'ali', 'dayili'))

	print(setOfNamesAgain)

