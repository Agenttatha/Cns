# Define the string
input_string = "Hello world"

# Initialize empty strings to hold the results
and_result = ''
xor_result = ''

# Perform AND and XOR operations on each character
for char in input_string:
    and_char = chr(ord(char) & 127)  # AND with 127
    xor_char = chr(ord(char) ^ 127)  # XOR with 127
    and_result += and_char
    xor_result += xor_char

# Display the results
print("Original string:", input_string)
print("Result after AND with 127:", and_result)
print("Result after XOR with 127:", xor_result)
