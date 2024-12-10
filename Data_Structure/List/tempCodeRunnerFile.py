def remove_duplicates(list_of_lists):
    unique_list = []
    seen = set()
    
    for sublist in list_of_lists:
        
        sublist_tuple = tuple(sublist)
        if sublist_tuple not in seen:
            unique_list.append(sublist)
            seen.add(sublist_tuple)
            
    return unique_list

my_list =[[10, 20], [40], [30, 56, 25], [10, 20], [33], [40]]
new_list = remove_duplicates(my_list)
print("New List: ",new_list)