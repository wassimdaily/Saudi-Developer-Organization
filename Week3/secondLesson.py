names = ['waseem', 'mousa', 'mohammed']
names2 = []
# print mousa and mohammed , 
print(names[1:3])

# check if student 'waseem' in the list of students or not

if 'waseem' in names:
	print('yes')
else:
	print('no matched')


# duplicate 'waseem' in the list

names2 = ['waseem'] * 2

addTwoDic = names + names2

print(addTwoDic) 
