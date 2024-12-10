def longest_word_length(words):
    if not words:
        return 0
    return max(len(word) for word in words)

sample_words = ["apple", "banana", "cherry", "pineapple"]

result = longest_word_length(sample_words)
print("Length of the longest word:", result)