# normal function without parameter

def printNames():
	names = ['waseem1', 'waseem2', 'waseem3', 'waseem4', 'waseem5']
	for i in range(len(names)):
		for x in names:
			c = -1
			print(names[c])
			c+=1
			break



# call the function the start the jop

printNames()

# parameterized

def printNames2(fName, sName):
	print('My first name is: '+fName)
	print('My second names is: '+sName)

printNames2('Waseem', 'Dayili')

def printNames3(fName = 'Waseem', sName = 'Dayili'):
        print('My first name is: '+fName)
        print('My second names is: '+sName)

printNames3()
	
