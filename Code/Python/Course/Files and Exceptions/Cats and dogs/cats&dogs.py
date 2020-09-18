try:
    cats = '/home/harry/Documents/Code-Learning/Code/Python/Course/Files and Exceptions/Cats and dogs/cats.txt'
    with open(cats, 'r') as f:
        print(f"\n")
        contents = f.readlines()
        for line in contents:
            print(f"{line.strip()}")
except FileNotFoundError:
    pass
try:
    dogs = '/home/harry/Documents/Code-Learning/Code/Python/Course/Files and Exceptions/Cats and dogs/dogs.txt'
    with open(dogs, 'r') as f:
        print(f"\n")
        contents = f.readlines()
        for line in contents:
            print(f"{line.strip()}")
except FileNotFoundError:
    pass
