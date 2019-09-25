# print my all characters by name & number of index Location

names = ['first', 'second', 'third', 'fourth', 'fiveth' ,'sixth']
array = ['w', 'a', 's', 'e', 'e', 'm']
indexX = 0
indexY = 0
for x in names:
	for y in array:
		print('My '+str(names[indexX])+' character is '+str(array[indexY]))
		indexX+=1
		indexY+=1
		break
print('Information about my name is contains of '+str(len(array))+' charactres are printed.')
