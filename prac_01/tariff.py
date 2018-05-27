tariff = float(input("Which tariff? 11 or 31: "))
TARIFF_11 = 0.244618
TARIFF_31 = 0.136928

if tariff == 11:
    tariff_cost = TARIFF_11
    print("tariff cost is ", TARIFF_11)

elif tariff == 31:
    tariff_cost = TARIFF_31
    print("tariff cost is ", TARIFF_31)

else:
    print("Invalid Command")

electricity_use=float(input("Enter the daily usage kWh: "))
billing_days=float(input("Enter the number of days included in billing: "))

total = tariff_cost * electricity_use * billing_days

print()
print("Electricity Bill Estimator 2.0")
print("Estimated bill: ${:.2f}".format(total))