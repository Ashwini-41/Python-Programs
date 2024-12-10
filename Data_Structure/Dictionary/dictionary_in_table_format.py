data = {"Name": "Ashwini", "Age": 20, "City": "Pune"}

# Print the dictionary in table format
print("{:<10} {:<10}".format("Key", "Value")) 
print("-" * 20) 
for key, value in data.items():
    print("{:<10} {:<10}".format(key, value)) 
