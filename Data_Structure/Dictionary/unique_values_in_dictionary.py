data = {
    "key1": "apple",
    "key2": "banana",
    "key3": "apple",
    "key4": "orange",
    "key5": "banana"
}

print(f"Dictionary : {data}")

# Use a set to extract unique values
unique_values = set(data.values())

print("Unique values in the dictionary:")
for value in unique_values:
    print(value)
