import random

numbers = 6
min_num = 1
max_num = 45

quick_picks = int(input("How many quick picks? "))
while quick_picks < 0:
    print("Invalid input")
    quick_picks = int(input("How many quick picks? "))

for i in range(quick_picks):
    quick_pick_numbers = []
    for n in range(numbers):
        random_num = random.randint(min_num, max_num)
        while random_num in quick_pick_numbers:
            random_num = random.randint(min_num, max_num)
        quick_pick_numbers.append(random_num)
    quick_pick_numbers.sort()
    print(" ".join("{:2}".format(random_num) for random_num in quick_pick_numbers))