from itertools import permutations

def generate_permutations(input_list):
    all_permutations = list(permutations(input_list))
    return all_permutations

input_list = [1,2,3,4]
result = generate_permutations(input_list)
print("Original list: ",input_list)
print("all permutations: ")
for ele in result:
    print(ele)