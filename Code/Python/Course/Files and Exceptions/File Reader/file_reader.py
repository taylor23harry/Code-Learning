file = '/home/harry/Documents/Code-Learning/Code/Python/Course/Files and Exceptions/File Reader/learning_python.txt'

with open(file) as file_object:
	lines = file_object.readlines()

contents = ''
for line in lines:
	contents += line
contents = contents.replace('Python', 'C')
print(contents)
