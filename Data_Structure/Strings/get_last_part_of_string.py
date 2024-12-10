def get_last_part_before_character(string, char):
    index = string.rfind(char)
    # If the character is found, return the substring before it
    if index != -1:
        return string[:index]
    # If the character is not found, return the original string
    return string

string1 = "https://www.w3resource.com/python-exercises"
string2 = "https://www.w3resource.com/python"

result1 = get_last_part_before_character(string1, "/")
result2 = get_last_part_before_character(string2, "h")

print("Result 1:", result1)
print("Result 2:", result2)
