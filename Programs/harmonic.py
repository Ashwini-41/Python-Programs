def harmonic_num():
    har = 0.0
    n = int(input("Enter number: "))
    
    for i in range(1,n):
        value = 1/i
        har = har + value
    
    print(f"Harmonic value is : {har :4f}")

harmonic_num()