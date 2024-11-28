# Reference substitution table (example)
substitution_table = {
    'a': 'm', 'b': 'n', 'c': 'o', 'd': 'p', 'e': 'q',
    'f': 'r', 'g': 's', 'h': 't', 'i': 'u', 'j': 'v',
    'k': 'w', 'l': 'x', 'm': 'y', 'n': 'z', 'o': 'a',
    'p': 'b', 'q': 'c', 'r': 'd', 's': 'e', 't': 'f',
    'u': 'g', 'v': 'h', 'w': 'i', 'x': 'j', 'y': 'k',
    'z': 'l', ' ': ' '  # Space remains unchanged
}

# Reverse substitution table for decryption
reverse_table = {v: k for k, v in substitution_table.items()}

# Function to encrypt a message
def encrypt_message(message):
    return ''.join(substitution_table.get(char, char) for char in message.lower())

# Function to decrypt a message
def decrypt_message(ciphertext):
    return ''.join(reverse_table.get(char, char) for char in ciphertext.lower())

# Main program
if __name__ == "__main__":
    print("1) Encrypt a message")
    print("2) Decrypt a message")
    print("3) Summarize the program")
    choice = input("Enter your choice (1/2/3): ").strip()
    
    if choice == '1':
        plaintext = input("Enter the message to encrypt: ").strip()
        ciphertext = encrypt_message(plaintext)
        print(f"Encrypted message: {ciphertext}")
    elif choice == '2':
        ciphertext = input("Enter the message to decrypt: ").strip()
        plaintext = decrypt_message(ciphertext)
        print(f"Decrypted message: {plaintext}")
    elif choice == '3':
        print("This program implements a substitution cipher. It can encrypt a plaintext message or decrypt a ciphertext message using a predefined substitution table.")
        user_summary = input("How would you summarize this program? ").strip()
        print(f"Your summary: {user_summary}")
    else:
        print("Invalid choice. Please run the program again.")
