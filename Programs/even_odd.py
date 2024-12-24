for i in range(1 , 21):
    if i % 2 == 0:
        print(i ," is a even number")
    else:
        print(i," odd number")

n = int(input("Enter number: "))
c = 0

for i in range(1,n+1):
    if n % i == 0:
        c= c+1
    
    if c >= 3:
        break
    
if c >= 3 :
    print(f"{n} is not a prime")
else:
    print(f"{n} is a prime")