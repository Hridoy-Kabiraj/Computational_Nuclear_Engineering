N = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 100, 1000, 10000]

for n in N:
    sum = 0.0
    fact = 1
    for j in range(n+1):
        if j > 0:
            fact *= j
        sum += 1/fact  
    print(f"The value of e for N={n} is {sum:.50f}\n")
