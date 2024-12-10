def prime_factors():
        N = int(input("Enter a positive integer N: "))

        if N <= 0:
            print("Error: Please enter a positive integer.")
            return

        print(f"Prime factors of {N} are:")

        while N % 2 == 0:
            print(2, end=" ")
            N //= 2

        i = 3
        while i * i <= N:
            while N % i == 0:
                print(i, end=" ")
                N //= i
            i += 2  

        if N > 2:
            print(N)


prime_factors()