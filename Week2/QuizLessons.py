def Process():
	message = 'Please, I want {} sandwished and {} donutes'
	process = message.replace('I', 'we')
	print("new message after replaced some words: "+process)
	print(message.format(5, 7))
	print(message.replace('a', 'A'))

Process()
