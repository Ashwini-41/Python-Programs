def find_triplets_with_zero_sum(arr) :
    n = len(arr)
    found_triplets = set()
    
    for i in range(n - 2):
        seen = set()
        for j in range(i + 1, n):
            target = -(arr[i] + arr[j])
            if target in seen:
                triplet = tuple(sorted((arr[i],arr[j],target)))
                found_triplets.add(triplet)
            else:
                seen.add(arr[j])
        
    print(f"Number of distinct triplets: {len(found_triplets)}")
    print("Distinct triplets that sum to zero:")
    for triplet in found_triplets:
        print(triplet)

   

N = int(input("Enter the number of integer : "))
if N < 3 :
    print("At least 3 integers are required to form triplets.")
else :
    print(f"Enter {N} integer: ")
    input_array = [int(input(f"Elemnet {i + 1}: ")) for i in range(N)]
    find_triplets_with_zero_sum(input_array)
