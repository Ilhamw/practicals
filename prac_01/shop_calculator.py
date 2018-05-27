num = int(input("Number of Item(s): "))
sum = 0

for num in range(num, 0, -1):
    price = float(input('Price of Item: $'))
    sum = sum + price

print("The total is ${:.2f}".format(sum))
