electricity_cost=float(input("Enter the cost per kWh in cents: "))
electricity_use=float(input("Enter the daily usage kWh: "))
billing_days=float(input("Enter the number of days included in billing: "))

total = electricity_cost/100 * electricity_use * billing_days

print()
print("Electricity Bill Estimator")
print("Estimated bill: ${:.2f}".format(total))