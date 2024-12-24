def find_min_max(input_file,output_file):
    with open(input_file,'r') as file:
        numbers = [int(line) for line in file]
        
        max_value = max(numbers)
        min_value = min(numbers)
        
        with open(output_file,'w') as file:
            file.write(f"Maximum value: {max_value}\n")
            file.write(f"Minimum value: {min_value}\n")
            
        print("Max and Min values written to the output file.")
    
input_file = "File_IO\ElementsOrNumbers.txt"
output_file = "File_IO\min_max_output.txt"
find_min_max(input_file,output_file) 