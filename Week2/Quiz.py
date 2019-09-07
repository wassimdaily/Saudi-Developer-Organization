def Process():
	message = 'Please, I want {} sandwished and {} donutes'
	process = message.replace('I', 'we')
	print("New message after replaced some words: "+process)
	print(message.replace('a', 'A'))
	print('insert some numbers to the main message: ')
	print(message.format(5, 7))

Process()
