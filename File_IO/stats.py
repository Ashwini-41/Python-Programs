import math

def calculate_mean(numbers):
    """Calculate the mean (average) of a list of numbers."""
    return sum(numbers) / len(numbers)

def calculate_sample_standard_deviation(numbers, mean):
    """Calculate the sample standard deviation of a list of numbers."""
    variance_sum = sum((x - mean) ** 2 for x in numbers)
    return math.sqrt(variance_sum / (len(numbers) - 1))

def read_numbers_from_file(input_file):
    """Read floating-point numbers from a file."""
    with open(input_file, 'r') as file:
        return [float(line.strip()) for line in file]

def write_stats_to_file(output_file, mean, std_dev):
    """Write the mean and standard deviation to a file."""
    with open(output_file, 'w') as file:
        file.write(f"Mean: {mean}\n")
        file.write(f"Sample Standard Deviation: {std_dev}\n")

def main():
    input_file = "File_IO/numbers.txt"  
    output_file = "File_IO/stats_output.txt"  

    numbers = read_numbers_from_file(input_file)

    mean = calculate_mean(numbers)
    std_dev = calculate_sample_standard_deviation(numbers, mean)

    write_stats_to_file(output_file, mean, std_dev)

    print(f"Mean and Sample Standard Deviation written to '{output_file}'.")

if __name__ == "__main__":
    main()
