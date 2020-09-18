import json
file = '/home/harry/Documents/Code-Learning/Code/Python/Course/Files and Exceptions/Verify User/user.json'

def update_name():
    """ Asks user for name and writes it to a json file """
    name = input("What's your name? : ")
    with open(file, 'w') as f:
        json.dump(name, f)
    return "Thanks! We'll remember that for the next time!"

try:
    with open(file) as f:
        content = json.load(f)
    answer = input(f"Hello, Is your name {content.title()}? :")
    if answer == 'yes' or 'Yes':
        print("Glad to hear it! Welcome back buddy :)")
    else:
        update_name()

except FileNotFoundError:
    print("User not found")
    update_name()
    
        
    