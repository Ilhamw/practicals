x = int(input("Enter the lowerbound(x) value: "))
y = int(input("Enter the upperbound(y) value: "))

MENU = """(1) Show the even numbers from x to y.
(2) Show the odd numbers from x to y
(3) Show the squares from x to y
(4) Exit program"""

print(MENU)
choice = str(input("Select an option>>> "))
while choice != "4":
    if choice == "1":
        if x % 2 == 0:
            for x in range(x, y+1, 2):
                print(x)
                x += 2
        else:
            for x in range(x+1, y+1, 2):
                x == x+1
                print(x)
                x += 2

    elif choice == "2":
        if x % 2 == 0:
            for x in range(x+1, y+1, 2):
                x == x+1
                print(x)
                x += 2
        else:
            for x in range(x, y+1, 2):
                print(x)
                x += 2

    elif choice == "3":
        for i in range(x, y+1):
            i *= i
            print(i)
            x += 1

    elif choice == "4":
        break

    else:
        print("Invalid Command")
    x = int(input("Enter the lowerbound(x) value: "))
    y = int(input("Enter the upperbound(y) value: "))
    print(MENU)
    choice = str(input("Select an option>>> "))

print("Finished")