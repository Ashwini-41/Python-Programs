def reverse_str(str):
    newstr = ""
    for char in str:
        newstr = char + newstr
    print("Reversed string : ",newstr)

def reverse_str2(str):
    reverse_text = ''.join(reversed(str))
    print(reverse_text)

str = "Ashwini"
reverse_str(str)
reverse_str2(str)