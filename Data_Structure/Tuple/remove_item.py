my_tuple = (1,2,3,4,5,6)

temp_list = list(my_tuple)

temp_list.remove(3)

my_tuple = tuple(temp_list)

print("Tuple after removing item: ",my_tuple)