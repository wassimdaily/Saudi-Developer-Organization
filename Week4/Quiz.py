# quiz q1 solution

set = {1, 3, 5, 7, 8}
newNum = {4, 8, 12}

for x in newNum:
	set.add(x)
print(set)

#######

# quiz q2 solution

dic = {'name': 'pigeon', 'type': 'bird', 'skin cover': 'feathers'}

# print type value
print(dic['type'])

# change skin cover value

dic['skin cover'] = 'human skin'

# show all items.

for x in dic:
	print('key-> '+str(x)+' value-> '+str(dic[x])) 
