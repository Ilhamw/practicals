num1 = int(input("Enter number: "))
num2 = int(input("Enter number: "))
num3 = int(input("Enter number: "))
num4 = int(input("Enter number: "))
num5 = int(input("Enter number: "))

min_num = min(num1, num2, num3, num4, num5)
max_num = max(num1, num2, num3, num4, num5)
avg_num = (num1 + num2 + num3 + num4 + num5) /5

print("""The first number is {}
The last number is {}
The smallest number is {}
The largest number is {}
The average number is {}""".format(num1, num5, min_num, max_num, avg_num))