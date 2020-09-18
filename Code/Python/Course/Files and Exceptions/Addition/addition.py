print("Enter 'q' to exit")
while True:
    print("I Add Numbers! select two numbers for me to add :D")
    number_1 = input("First Number : ")
    if number_1 == 'q':
        break
    number_2 = input("Second Number : ")
    if number_2 == 'q':
        break

    try:
        result = int(number_1) + int(number_2)
    except ValueError:
        print("\n\tYou can't add anyting other than a number!\n")
    else:
        print(f"\n\t{result}\n")