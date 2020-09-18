file = '/home/harry/Documents/Code-Learning/Code/Python/Course/Files and Exceptions/Guest/guest.txt'
name = input("Hey! What's your name? : ")

with open(file, 'w') as file_object:
	file_object.write(name)
