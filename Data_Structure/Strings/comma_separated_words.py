words = input("Enter a comma-separated sequence of words: ")

word_list = words.split(", ")

unique_words = set(word_list)

# Sort the unique words alphanumerically
sorted_words = sorted(unique_words)

# Join the sorted words back into a comma-separated string
result = ", ".join(sorted_words)

print("Sorted unique words:", result)
