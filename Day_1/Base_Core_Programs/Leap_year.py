def leap_year() :
    year = int(input("Enter year : "))
    
    if year % 4 == 0 and year % 100 != 0:
        print("Leap year")
    elif year % 400 == 0 :
        print("Leap year")
    elif year % 16 == 0 :
        print("Leap year")
    else :
        print("Not a leap year")
        
leap_year()