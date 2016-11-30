cents =str(input("Enter cents per kWh:"))
daily =float(input("Enter daily use in kWh:"))
days =float(input("Enter number of billing days:"))
bill = (cents * daily * days)/100
print("Estiater bill:$", bill)
