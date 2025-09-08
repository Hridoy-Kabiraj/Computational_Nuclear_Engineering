import math

x = float(input("Enter a number: "))

y = x**(1/3)

print(f"The cubic root of {x} is {y}")
print(f"The accuracy is {(1 - math.fabs((round(y)-y)))*100}%")
