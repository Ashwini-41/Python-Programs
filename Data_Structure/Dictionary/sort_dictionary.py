# Write a Python script to sort (ascending and descending) a dictionary by
# value.

my_dict = {1:25,2:40,3:10,4:35}
print("Ascending: ",dict(sorted(my_dict.items(), key = lambda x:x[1])))
print("Descending:", dict(sorted(my_dict.items(), key=lambda x: x[1], reverse=True)))

#2. Add a key to a dictionary.
my_dict[3] = 88
print("Updated dictionary: " , my_dict)

#iterate over dictionaries using a for loop.

for key, value in my_dict.items():
    print(f"key : {key}, Value : {value}")
 
#Generate and print a dictionary (x, x*x) 
n = 5
square_dict = {x:x**2 for x in range(1,n+1)}
print("Squared Dictionary : ",square_dict)  

#Remove a key from dictionary
my_dict.pop(1)
print("Dictionary after removing key 1:", my_dict)



