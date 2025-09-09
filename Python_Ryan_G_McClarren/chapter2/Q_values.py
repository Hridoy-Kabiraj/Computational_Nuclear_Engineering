r1 = float(input("Enter the mass of first reactant in amu: "))
r2 = float(input("Enter the mass of second reactant in amu: "))


p1 = float(input("Enter the mass of first product in amu: "))
p2 = float(input("Enter the mass of second product in amu: "))

Q_value = ((r1 + r2) - (p1 + p2)) * 931.494061

print(f"The Q value of the reaction is {Q_value} MeV")