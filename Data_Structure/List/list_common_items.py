def find_common_items(list1, list2):
    common_items = [item for item in list1 if item in list2]
    return common_items

def common_ele(list1,list2):
    common_numbers = list(set(list1) & set(list2))
    return common_numbers

list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]

common_items = find_common_items(list1, list2)
print("Common items1:", common_items)

common_items2 = common_ele(list1, list2)
print("Common items2:", common_items2)

