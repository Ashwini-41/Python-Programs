import math 

x = int(input("Enter the x-coordinate: "))
y = int(input("Enter the y-coordinate: "))

distance = math.sqrt(x**2 + y**2)

print(f"The Euclidean distance from ({x}, {y}) to the origin (0, 0) is: {distance:.2f}")
