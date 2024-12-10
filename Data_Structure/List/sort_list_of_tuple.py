my_list = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]

# Sort the list using the last element of each tuple as the key
sorted_list = sorted(my_list, key=lambda x: x[-1])

print("Sample List:", my_list)
print("Sorted List:", sorted_list)
