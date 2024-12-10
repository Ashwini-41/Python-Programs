import textwrap

sample_text = "Python is an interpreted, high-level, and general-purpose programming language. Its design philosophy emphasizes code readability with the use of significant indentation."

# Format the text with width=50
formatted_text = textwrap.fill(sample_text, width=50)

print("Formatted Text:\n")
print(formatted_text)
