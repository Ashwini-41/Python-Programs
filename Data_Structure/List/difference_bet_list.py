def list_difference(list1, list2):
    difference = [item for item in list1 if item not in list2]
    return difference

list_a = [1, 2, 3, 4, 5]
list_b = [4, 5, 6, 7, 8]

difference = list_difference(list_a, list_b)

print("List A:", list_a)
print("List B:", list_b)
print("Difference (elements in List A but not in List B):", difference)
