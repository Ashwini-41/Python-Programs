import math

a = float(input("Enter the value of a (coefficient of x^2): "))
b = float(input("Enter the value of b (coefficient of x): "))
c = float(input("Enter the value of c (constant): "))

delta = b**2 - 4*a*c

if delta > 0 :
    root1 = (-b + math.sqrt(delta)) / (2 * a)
    root2 = (-b - math.sqrt(delta)) / (2 * a)
    print(f"The roots of the quadratic equation are real and distinct:")
    print(f"Root 1: {root1:.2f}")
    print(f"Root 2: {root2:.2f}")
elif delta == 0:
    root = -b / (2 * a)
    print(f"The roots of the quadratic equation are real and equal:")
    print(f"Root: {root:.2f}")
else:
    real_part = -b / (2 * a)
    imaginary_part = math.sqrt(-delta) / (2 * a)
    print(f"The roots of the quadratic equation are complex:")
    print(f"Root 1: {real_part:.2f} + {imaginary_part:.2f}i")
    print(f"Root 2: {real_part:.2f} - {imaginary_part:.2f}i")