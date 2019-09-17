# for, while loops
# print 
i = 1

while(i<=10):	
	print('number loop: '+str(i))
	i = i+1


file = open('file.txt').readlines()
for x in file:
	print('Name:'+x)
	if x is None:
		break

for y in file:
	if y == 'Randa':
		print(y)
		continue

cond = 0
while cond < 6:
		print(cond)
		cond+=1
else:
		print('cond is ni longer less than 6')
