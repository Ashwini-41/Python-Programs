def factors() :
    N = int(input("Enter number : "))
    
    fact = 1
    for i in range(1,N+1) :
        fact *= i
        
    print(fact)
    
factors()