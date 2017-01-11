class Guitars:
    def __init__(self, name="", year=0, cost=0):
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        return "{}({}) : ${:.2f}".format(self.name, self.year, self.cost)

    def get_age(self):
        current_year = 2017
        age = current_year - int(self.year)
        if age >= 50:
            vintage = True
        else:
            vintage = False
        return vintage

print("My guitars!")
guitars = []
guitar_name = input("Name:")
while guitar_name !="":
    guitar_year = str(input("Year:"))
    guitar_cost = float(input("Cost:"))
    guitar_info = [guitar_name, guitar_year, guitar_cost]
    guitars.append(guitar_info)
    print("{} added".format(Guitars(guitar_name, guitar_year, guitar_cost)))

    guitar_name = input("Name:")
count =1
print("These are my guitars:")

for i in guitars:
    info = Guitars(i[0], i[1], i[2])
    age = info.get_age()
    if age == True:
        print("Guitar {}: {} (vintage)".format(count,info))
    else:
        print("Guitar {}: {}".format(count,info))
    count +=1