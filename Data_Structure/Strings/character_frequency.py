sample_string = "googleclassromm"

char_freq = {}

for char in sample_string:
    if char in char_freq:
        char_freq[char] += 1
    else:
        char_freq[char] = 1

print("Character frequency in the string:", char_freq)        
