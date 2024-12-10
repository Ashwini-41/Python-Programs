my_list = [10,20,30,40,10,20,50,60,30]

new_list = set()

for i in range(len(my_list)) :
    new_list.add(my_list[i])
  
print(f"Originl list: ",my_list)
list_dist = list(set(new_list))  
print(f"List without duplicate element:" , new_list)
print("List without duplicate element:",list_dist)