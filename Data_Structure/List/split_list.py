def split_list_by_first_char(words):
    result = {}
    
    for word in words:
        first_char = word[0]
        if first_char not in result:
            result[first_char] = [word]
        else:
            result[first_char].append(word)
        
    return result

words = ['apple', 'banana', 'avocado', 'berry', 'cherry', 'cantaloupe']
split_words = split_list_by_first_char(words)
print("Words split by first character:", split_words)
            