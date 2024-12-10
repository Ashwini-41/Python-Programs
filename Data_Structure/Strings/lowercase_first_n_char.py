
def lowercase_first_n_chars(s,n):
    if n > len(s):
        n = len(s)
    return s[:n].lower() + s[n:]

string = "PYTHON IS Amazing!"
n = 8

modified_string = lowercase_first_n_chars(string, n)

print("Original String:", string)
print("Modified String:", modified_string)
