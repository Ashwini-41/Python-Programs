
dic1 = {1: 10, 2: 20}
dic2 = {3: 30, 4: 40}
dic3 = {5: 50, 6: 60}

# Concatenate dictionaries using the update() method
result = {}
result.update(dic1)  
result.update(dic2)  
result.update(dic3)  

# Print the concatenated dictionary
print("Concatenated Dictionary:", result)
