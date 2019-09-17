# start from 0 to 9
print('start from 0 to 9') 
for x in range(10):
	print(x)
else:
	print('finished')

# strat form 1 to 9
print('strat form 1 to 9')
for y in range(1,10):
	print(y)
else:
	print('finished')

# start form 1 to 9 with increase by 2 every round cycle
print('start form 1 to 9 with increase by 2 every round cycle')
for z in range(1,10,2):
	print(z)
else:
	print('finished')




students = ['waseem', 'othman', 'faisal', 'naser']
GPA = [4.80, 3.83, 2.23, 3.12]
i = 0

# 2 for loops to extract and print elements [students & gpa]
for x in students:

	i+=len(students)

	print('Student name: ' + str(students[i]))

	for y in GPA:

		print('Gpa: ' + str(GPA[i]))
		break

