# Note:: you should use python version 3.3 to use this program
# students list

names = ['waseem', 'othman', 'omran', 'osamah']
id    = ['201503234', '201603234', '201703234', '201803234']

# get numbers of students
print('the number of students is: ' + str(len(names)))

# add new student

names.append('rawan')
id.append('201903234')
print("there're new student: "+str(names)+'\n'+'with new id is: '+str(id))

# add new student his number start of date 2015 should be in seiries elemets
names.insert(1, 'samira')
id.insert(1, '201503235')
print(names)
print(id)

# remove/delete a student

names.remove('omran')
print("new list after delete 'omran' :" +str(names))

# pop/remove/delete id of student 'omran' indexed with 3 in id list

print('before: '+str(id))
id.pop(3)
print('after: '+str(id))

# now delete last on of the list stdeunts

names.pop()
print(names)

# delete all list of students and check after clear is empty or not

# strat to clear

names.clear()
id.clear()

if names and id == []:
	print('the list empty')
else:
	print("there're elements in the list")

# copy list by values not by reference by using copy list attribute.
# there're two types of way to copy list by using copy & list
namesCopy = names.copy()

print(names)
print(namesCopy)

idCopy = id.list()

print(idCopy) 
