# copy the dictionary by using some fucntions such as copy() & dict() all same method.

names = {'std1': 'waseem', 'std2': 'ahmed', 'std3': 'ali'}

# copy by using copy() function and dict.

copyNames = names.copy()
copyNames2 = dict(names)

print(copyNames)
print(copyNames2)

# nested dictionaries.

mainDict = {

'usernames' : {
'user1': 'waseem',
'user2': 'dragon1997'
},
'passwords' : {
'pass1': '123456',
'pass2': '076382'
}
}

print(mainDict)
