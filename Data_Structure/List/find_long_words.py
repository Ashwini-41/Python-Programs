def find_long_words(sample_words,n) :
    long_words = [word for word in sample_words if len(word) > n]
    return long_words

sample_word = ["ashwini","Shree","adi","pray","vaishuu","johner"]
n = 5
print("Original list : ",sample_word)
print("List of long words: ",find_long_words(sample_word,n))