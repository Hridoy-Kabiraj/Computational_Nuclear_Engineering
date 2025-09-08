sum = 0
print("The multiples of 3 and 7 under 10000 are:\n")
for i in range(10000):
    if i%3==0 or i%7==0:
        sum += i
        if i != 0:
            print(i)

print(f"\n The sum of the numbers is: {sum}")
