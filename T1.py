
amount1 = float(input("Enter a value "))
amount2 = float(input("Enter a value "))

if amount1 > 10 and amount2 < 100:
    if amount1 > amount2:
        print(amount1)
    else:
        print(amount2)

le1 = float(input("Enter the length of the triangle 1 "))
wi1 = float(input("Enter the width of the triangle 1 "))
le2 = float(input("Enter the length of the triangle 2 "))
wi2 = float(input("Enter the width of the triangle 2 "))
area1 = (le1 * wi1) / 2
area2 = (le2 * wi2) / 2
if area1 > area2:
    print('The area of Triangle 1 is greater')
elif area2 > area1:
    print(' The area of Triangle 2 is greater')
elif area1 == area2:
    print('The area of two triangles are the same')
