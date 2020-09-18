import json
file = '/home/harry/Documents/Code-Learning/Code/Python/Course/Files and Exceptions/Favourite Number/favourite_number.json'

try:
    with open(file) as f:
        num = json.load(f)
        print(f"Your favourite number is {num}")
except FileNotFoundError:
    with open(file, 'w') as f:
        num = input("It seems that I don't know your favourite number, What is it? ")
        json.dump(num, f)
        print(f"Thank you, we will remember '{num}' for next time.")
