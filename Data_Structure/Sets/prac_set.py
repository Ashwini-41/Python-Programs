#craete set
my_set = {1, 2, 3, 4, 5}
print("Set:", my_set)

#Iterate over a set.
for item in my_set:
    print(item)

#  Add members to a set.
my_set.add(6)
my_set.update([7, 8])
print("Updated Set:", my_set)

# Remove items from a set.
my_set.discard(7)  
print("Set after removing 7:", my_set)

# Create union, intersection, and symmetric difference.
set1 = {1, 2, 3}
set2 = {3, 4, 5}
print("Union:", set1 | set2)
print("Intersection:", set1 & set2)
print("Symmetric Difference:", set1 ^ set2)
