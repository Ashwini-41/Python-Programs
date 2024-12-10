

# name = input("Enter you name : ")
# print(f"Hello {name} , How are you? ")

def replaceString(username) :
    while len(username) < 3:
        print("Invalid user name")
        username = input("Enter your name : ")
        
    template = "Hello <<username>> , How are you? "
    result = template.replace("<<username>>",username)
    print(result)
    
# replaceString("Ashwini")
name = input("Enter your name (minimum 3 characters): ")
replaceString(name)

