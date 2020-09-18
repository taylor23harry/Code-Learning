file = '/home/harry/Documents/Code-Learning/Code/Python/Course/Files and Exceptions/Guest/guest_book.txt'

while True:
    current_name = input("Hello! What's your name?")
    print(f"Welcome {current_name.title()} You have been added to the Guest Book")
    with open(file, 'a') as f:
        f.write(f"{current_name.title()}\n")
