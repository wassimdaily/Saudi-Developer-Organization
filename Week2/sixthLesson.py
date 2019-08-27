n1 = 20
n2 = 43

if n2 > n1 and n1<30:
	print('yes')
else:
	print('no')

if n2 > n1 or n1==30:
        print('yes')
else:
        print('no')

if not(n2 > n1): # must reslut return false
	print('yes')
else:
	print('no')

if n1 is n2:
	print('yes n1 is n2')
else:
	print("n1 is't n2")

if n1 is not n2:
	print('yes n1 is not n2')
else:
	print('no n1 is n2')
numbers = [1,2,3,4,5,6,7,8,233,2343]

if n1 in numbers:
	print('YES')
else:
	print('NO')

if n1 not in numbers:
	print('YES')
else:
	print('NO')

