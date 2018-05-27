LOWER_BOUND = 33
UPPER_BOUND = 127

character = str(input("Enter a character: "))
print("The ASCII code for {} is {}".format(character, ord(character)))
order = int(input("Enter a number between {} and {}: ".format(LOWER_BOUND, UPPER_BOUND)))

while order < LOWER_BOUND or order > UPPER_BOUND:
    order = int(input("Enter a number between {} and {}: ".format(LOWER_BOUND, UPPER_BOUND)))

print("The character for {} is {}".format(order, chr(order)))


