#1
name = str(input("Enter your name: "))

OUTPUT_FILE = "name.txt"
out_file = open(OUTPUT_FILE, 'w')
print("Your name is {}".format(name), file=out_file)
out_file.close()

#2
result = open(OUTPUT_FILE, 'r')
name = result.read()
print(name)
result.close()

#3
numbers = open("numbers.txt", 'r')
num1 = int(numbers.readline())
num2 = int(numbers.readline())
total = num1 + num2
print(total)
numbers.close()

#4
numbers = open("numbers.txt", 'r')
sum = 0
for line in numbers:
    number = int(line)
    sum += number
print(sum)
numbers.close()