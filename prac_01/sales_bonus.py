sales = float(input("Enter Sales= $"))

while sales >= 0:

    if sales < 1000 and sales >=0:
        bonus=0.1*sales

    elif sales >= 1000:
        bonus=0.15*sales

    else:
        print("Invalid command")

    print("Bonus is ${}".format(bonus))
    sales = float(input("Enter Sales= $"))


print("Thank you.")