# Define the string
input_string = "Hello world"

# XOR each character in the string with 0
result = ''.join([chr(ord(char) ^ 0) for char in input_string])

# Display the result
print("Original string:", input_string)
print("Result after XOR with 0:", result)
