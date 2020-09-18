file = '/home/harry/Documents/Code-Learning/Code/Python/Course/Files and Exceptions/File Reader/common_words.txt'
with open(file, 'r') as f:
    content = f.read()
    print(content.lower().count('the '))
