def vigenere_encrypt(plaintext, key):
    # Convert to lowercase
    plaintext = plaintext.lower()
    key = key.lower()
    
    # Extend the key to match the length of the plaintext
    extended_key = (key * (len(plaintext) // len(key))) + key[:len(plaintext) % len(key)]
    
    ciphertext = ""
    for p_char, k_char in zip(plaintext, extended_key):
        # Perform the Vigenère cipher encryption
        encrypted_char = chr(((ord(p_char) - ord('a') + ord(k_char) - ord('a')) % 26) + ord('a'))
        ciphertext += encrypted_char
    
    return ciphertext


def vigenere_decrypt(ciphertext, key):
    # Convert to lowercase
    ciphertext = ciphertext.lower()
    key = key.lower()
    
    # Extend the key to match the length of the ciphertext
    extended_key = (key * (len(ciphertext) // len(key))) + key[:len(ciphertext) % len(key)]
    
    plaintext = ""
    for c_char, k_char in zip(ciphertext, extended_key):
        # Perform the Vigenère cipher decryption
        decrypted_char = chr(((ord(c_char) - ord('a') - (ord(k_char) - ord('a'))) % 26) + ord('a'))
        plaintext += decrypted_char
    
    return plaintext


# Example usage:
plaintext = "GEEKSFORGEEKS"
key = "AYUSHAYUSHAYU"

encrypted_text = vigenere_encrypt(plaintext, key)
print("Encrypted Text:", encrypted_text)

decrypted_text = vigenere_decrypt(encrypted_text, key)
print("Decrypted Text:", decrypted_text)
