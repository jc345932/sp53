item =int(input("How many items:"))
while item < 0:
    print("Invalid number of items!")
    item = int(input("How many items:"))
cost =int(input("How much for item:"))
while cost < 0:
    print("Invalid prices")
    cost = int(input("How much for item:"))
total = cost * item
if total > 100:
    total = total * 0.9
else:
    total = total
print("Total is:$", total)