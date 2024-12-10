my_tuple = (1, 2, 3, 4, 1, 2, 5, 6, 1)

repeated_item = []
for item in my_tuple:
    if my_tuple.count(item) > 1 and item not in repeated_item:
        repeated_item.append(item)
    
print("Repeated items in tuple : ",repeated_item)