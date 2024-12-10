def harmonic_number() :
    num1 = int(input("Enter a number : "))
    
    harmonic_sum = 0.0

    for i in range(1,num1) :
        value = 1 / i
        harmonic_sum += value
        
    print(f"Harmonic value is : {harmonic_sum : 6f}")

harmonic_number()