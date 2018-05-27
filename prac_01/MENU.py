name=str(input("Enter name: ".title()))
MENU = """(H)ello
(G)oodbye
(Q)uit"""

print(MENU)
choice = input(">>> ".capitalize())
while choice != "Q":
    if choice == "H":
        print("Hello", name)

    elif choice == "G":
        print("Goodbye", name)

    else:
        print("Invalid Command")

    print(MENU)
    choice = input(">>> ".capitalize())


print("Finished")