from math import sqrt
a = float(input(" Type a real number a "))
b = float(input(" Type a real number b "))
c = float(input(" Type a real number c "))
if a == 0:  # That means bx+c=0 which is the linear equation
    if b == 0:  # That means we end with c=0
        if c == 0:
            print('All solution')
        else:  # means c != 0
            print('No solution')
    else:  # means b != 0
        print(" The solution is ", -c/b)
    # skip
else:  # means a is not = 0
    d = b*b - 4*a*c
    if d > 0:
        x1 = (-b+sqrt(d))/(2*a)
        x2 = (-b-sqrt(d))/(2*a)
        print("The solutions are:", x1, 'and', x2)
    elif d == 0:
        x = (-b)/(2*a)
        print(" The solution is ", x)
    else:
        print("No real number solution")
