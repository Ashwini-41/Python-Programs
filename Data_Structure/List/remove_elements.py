def remove_elemets(sample_list):
    return [item for index,item in enumerate(my_list) if index not in(0,4,5)]

my_list =  ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
result = remove_elemets(my_list)

print("Original List:", my_list)
print("Modified List:", result)