def create_and_print_2D_array() :
    row = int(input("Enter row number :"))
    col = int(input("Enter col number : "))
    
    if row <= 0 or col <= 0 :
        print("Please enter valid number")
        return
    
    arr_2D = []
    
    print("Enter elements of array : ")

    for i in range(row) :
        R = []
        for j in range(col) :
            element = int(input())
            R.append(element)
        arr_2D.append(R)
    
    print("2D Array : ")
    for ele in arr_2D :
        print(ele)
        
create_and_print_2D_array()