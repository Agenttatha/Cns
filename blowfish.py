from Crypto.Cipher import Blowfish
from Crypto.Util.Padding import pad, unpad
from secrets import token_bytes

# Function to generate a random key for Blowfish encryption
def generate_key():
    return token_bytes(16)  # Blowfish supports keys between 4 and 56 bytes

# Function to encrypt the plaintext using Blowfish
def encrypt(plaintext, key):
    cipher = Blowfish.new(key, Blowfish.MODE_ECB)
    padded_text = pad(plaintext.encode('utf-8'), Blowfish.block_size)
    ciphertext = cipher.encrypt(padded_text)
    return ciphertext

# Function to decrypt the ciphertext using Blowfish
def decrypt(ciphertext, key):
    cipher = Blowfish.new(key, Blowfish.MODE_ECB)
    decrypted_text = unpad(cipher.decrypt(ciphertext), Blowfish.block_size)
    return decrypted_text.decode('utf-8')

# Example usage of Blowfish algorithm
if __name__ == '__main__':
    key = generate_key()
    print("Key:", key.hex())

    plaintext = "HELLO BLOWFISH"
    print("Original text:",
