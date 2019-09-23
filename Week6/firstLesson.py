def displayList(par):
	for x in par:
		print(x)
	return "the lst has been done"



List = ['waseem', 'ahmed', 'ali', 'dayili']

displayList(List)


# get square of number 

def square(num):
	print('---------------------------')
	return 'equal to ' + str(num * num)


print(square(2))

# get some of four differents numbers

def getSome(num1, num2, num3, num4):
	return num1+num2+num3+num4


getSome(1, 2, 3, 4)


def jj(*tub):
	for x in tub:
		print(x)

jj('waseem', 'ahmed', 'ali', 'dayili')


# recursion function

# function that calls itself
		
