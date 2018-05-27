CURRENT_YEAR = 2018
VINTAGE_AGE = 50

class Guitar():

    def __init__(self, name, year, cost):
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        return "{} ({}) : {}".format(self.name, self.year, self.cost)

    def get_age(self):
        age = CURRENT_YEAR - self.year
        return age

    def is_vintage(self):
        return self.get_age() >= VINTAGE_AGE

    def __lt__(self, other):
        """Less than, used for sorting Guitars by year released."""
        return self.year < other.year