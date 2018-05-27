def main():
    """Get name thing, without functions."""
    name = get_name()

    print_name(name, 3)


def print_name(name, step=2):
    print(name[::step])


def get_name():
    name = input("Name: ")
    while name == "":
        print("Invalid name.")
        name = input("Name: ")
    return name

main()