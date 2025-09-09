def two_by_two_solver(a1, b1, c1, a2, b2, c2, LOUD = False):
    new_b2 = b2 - a2/a1*b1
    new_c2 = c2 - a2/a1*c1

    y = new_c2/new_b2

    x = (c1 - b1 * y) / a1

    if (LOUD):
        print(f"Th e solution to \n {a1}x + {b1}y = {c1}\n {a2}x + {b2}y = {c2}\n is x = {x} , y = {y}")
    return [x, y]

two_by_two_solver(4.5,3,10.5,1.5,3,7.5,True)