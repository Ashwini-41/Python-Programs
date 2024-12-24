frozen_set1 = ({1,2,34,5,6,76,4})
frozen_set2 =({10,20,2,45,5,34,78,98})

print("Intersection : ", frozen_set1.intersection(frozen_set2) )
print("Union: ",frozen_set1.union(frozen_set2))
print("Difference: ",frozen_set1.difference(frozen_set2))

try:
    frozen_set2.add(99)
except AttributeError as e:
    print("Error: ",e)