def main():
    global score
    score = float(input("Enter score: "))
    print(print_grade(score))


def print_grade(score):
    if score >= 50 and score < 90:
        return("Passable")
    elif score > 90 and score <= 100:
        return("Excellent")
    elif score < 50 and score >= 0:
        return("Bad")

    else:
        return("Invalid score")


main()