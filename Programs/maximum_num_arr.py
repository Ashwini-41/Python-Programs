# Input: Array elements
arr = list(map(int, input("Enter array elements separated by spaces: ").split()))

# Initialize the maximum element with the first element of the array
max_element = arr[0]

# Iterate through the array to find the maximum
for num in arr:
    if num > max_element:
        max_element = num

# Print the maximum element
print(f"The maximum element in the array is: {max_element}")

