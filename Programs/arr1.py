arr = list(map(int,input("Enter elemets: ").split()))

max_num = arr[0]
sec_max = arr[0]
for i in arr:
    if i > max_num:
        sec_max = i
        max_num = i
    
print("Maximum number: ",max_num)