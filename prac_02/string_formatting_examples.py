name = "Gibson L-5 CES"
year = 1922
cost = 16035.40

print("My guitar: " + name + ", first made in " + str(year), '\n')

print("My guitar: {}, first made in {}".format(name, year))
print("My guitar: {0}, first made in {1}".format(name, year))
print("My guitar: {0}, first made in {1} (that's right, {1}!)".format(name, year), '\n')

print("My {} would cost ${:,.2f}".format(name, cost))

