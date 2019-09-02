# single value in tuble
singleT = ('waseem',)
print(singleT)

# multi values in tuble
multiT = ('waseem', '21', 1090.83)
print(multiT)

# call specific value by index
print(multiT[0]) # print my name 'waseem'
print(multiT[0:2])
# print all values of the tuble
for getAll in multiT:
	print(getAll)

# delete & remove the last tubles

del singleT
del multiT
