
create_set = {1,2,3,4,5,6}

imutable_set = frozenset(create_set)

print(f"Frozen Set : {imutable_set}")

try :
    imutable_set.add(6)
except AttributeError as e :
    print("Error ",e)

frozen_set = ({3,1,9,27,10,5})

print("Union of frozenset :" , imutable_set.union(frozen_set))
print("Intersection of frozenset: ",imutable_set.intersection(frozen_set))
print("Difference of two sets: ",imutable_set.difference(frozen_set))