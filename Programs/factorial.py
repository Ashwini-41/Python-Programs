n = int(input("Enter number: "))
fact = 1

for i in range(1,n+1):
    fact = fact * i
    print(i)
    
print(f"Factorial of {n} is : ",fact)