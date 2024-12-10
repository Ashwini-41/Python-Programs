def add_suffix(str):
    
    if len(str) < 3:
        return str
    elif str.endswith('ing'):
        return str + 'ly'
    else:
        return str + 'ing'

String1 = "abc"
String2 = "String"

print(f"Result for {String1} is ",add_suffix(String1))
print(f"Result for {String2} is ",add_suffix(String2))
