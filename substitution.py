import string

def create_substitution_alphabet(key):
    alphabet = string.ascii_lowercase
    key = key.lower()
    key_unique = ''.join(sorted(set(key), key=key.index))
    substitution_alphabet = key_unique + ''.join(sorted(set(alphabet) - set(key_unique)))
    return substitution_alphabet

def substitution_cipher(text, key, mode='encrypt'):
    substitution_alphabet = create_substitution_alphabet(key)
    alphabet = string.ascii_lowercase
    if mode == 'encrypt':
        mapping = str.maketrans(alphabet, substitution_alphabet)
    else:
        mapping = str.maketrans(substitution_alphabet, alphabet)
    return text.translate(mapping)

# Example usage
if __name__ == "__main__":
    original_text = "hello"
    key = "cipher"
    encrypted_text = substitution_cipher(original_text, key, mode='encrypt')
    print("Encrypted:", encrypted_text)
    decrypted_text = substitution_cipher(encrypted_text, key, mode='decrypt')
    print("Decrypted:", decrypted_text)
