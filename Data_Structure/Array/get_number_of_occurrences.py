# Write a Python program to get the number of occurrences of a specified element in an
# array.
my_arr = [1,2,3,4,3,5,1,7,3]

element = 3
print(f"Occurrences of {element}:" , my_arr.count(element)) 

for i in range(len(my_arr)) :
    print(f"Occurrences of {my_arr[i]} : " ,my_arr.count(my_arr[i]))
    
