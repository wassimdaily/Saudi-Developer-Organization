cars = ('GTR-Nissan', 'Firarry', 'TOYOTA')

# check the car

if 'GTR-Nissan' in cars:
	print('yes')
else:
	print('no')

# duplicate single value of the tuple

model_id = (2019, ) * 4
print(model_id)

# merge two tuples together in one tuple

mergeTuples = cars + model_id
print(mergeTuples)

# example

x = (3, 4, 5, 6)
x = x + (1, 2, 3)
print(x)

# calculate length of my tuple by using len function
print('we have '+str(len(cars))+' car.')

# create a tuple by using tuple fuction.
print( tuple(('waseem', 'ahmmed', 'ali', 'dayili')) ) 


# example to convert list to tuple

dataSet = ['waseem', 'dayili']
print(type(dataSet)) # as you can see the type of the varibale is list

# right now convert it to tuple
print(type(tuple(dataSet)))

""" 
as you can see the type of the variable dataSet is 'tuple' right now,
because we're convert the list to tuple by using tuble function.
"""

###################################### tuple methods ######################


# use count and index()
# count how much the element is setting in the tuble
print(tuple(('w', 's', 's', 's', 'w', 'w')).count('w'))

# find the index or location of the element in memory&tuple 'waseem'

print(tuple(('othman', 'omran', 'waseem', 'rawan', 'ali')).index('waseem'))
