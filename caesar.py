def caesar_cipher(text, shift, mode='encrypt'):
    result = ''
    if mode == 'decrypt':
        shift = -shift
    for char in text:
        if char.isalpha():
            ascii_offset = ord('A') if char.isupper() else ord('a')
            shifted_char = chr((ord(char) - ascii_offset + shift) % 26 + ascii_offset)
            result += shifted_char
        else:
            result += char
    return result

# Example usage
if __name__ == "__main__":
    original_text = "Hello, World!"
    shift_value = 3
    encrypted_text = caesar_cipher(original_text, shift_value, mode='encrypt')
    print("Encrypted:", encrypted_text)
    decrypted_text = caesar_cipher(encrypted_text, shift_value, mode='decrypt')
    print("Decrypted:", decrypted_text)
