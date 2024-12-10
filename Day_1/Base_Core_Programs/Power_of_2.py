def power_of_2() :
    number = int(input("Enter number : "))
    if 0 <= number < 31 :
        print(f"Table of 2 up to power 2^{number}")
        for i in range(number + 1) :
            print(f"2^{i} = {2 ** i}")
    else :
        print("Error: N must be in the range 0 to 30 inclusive.")

power_of_2()
