def append_list(list1,list2):
    list1.extend(list2)
    return list1

list_a = [1, 2, 3]
list_b = [4, 5, 6]

result = append_list(list_a, list_b)

print("List A after appending List B:", result)