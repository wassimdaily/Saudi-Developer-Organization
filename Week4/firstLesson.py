proLang = {'python', 'java', 'php', 'ruby', 'dart'}

for x in proLang:
	print(x + ' is programming language.')


# to check and match the specific word in the list 


if 'python ' in proLang:
	print('yes')

else:
	print('no')

# add new programming language to the set

proLang.add('java script')
proLang.add('node js')
print(proLang)

# add three new programming languages.

proLang.update(['sql', 'c++', 'c#'])
print('all programming languages are: ')
for y in proLang:
	print(y)
