sample_list = ['abc', 'xyz', 'aba', '122']

count = 0

for string in sample_list:
    if len(string) >= 2 and string[0] == string[-1]:
        count += 1

print("Sample List:", sample_list)
print("Number of matching strings:", count)
