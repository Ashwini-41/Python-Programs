my_string = "restart"

first_char = my_string[0]

result_string = first_char + my_string[1:].replace(first_char,'$')

print("Input String: ",my_string)
print("Result string: ",result_string)