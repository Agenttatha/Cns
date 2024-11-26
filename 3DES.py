from Crypto.Cipher import DES3
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad
import binascii

# Function to encrypt text using 3DES
def encrypt_3des(plain_text, key):
    cipher = DES3.new(key, DES3.MODE_CBC)  # Create a new 3DES cipher in CBC mode
    padded_data = pad(plain_text.encode(), DES3.block_size)  # Pad the data to match block size
    cipher_text = cipher.encrypt(padded_data)  # Encrypt the padded data
    return cipher.iv + cipher_text  # Return IV + ciphertext for decryption

# Function to decrypt 3DES ciphertext
def decrypt_3des(cipher_text, key):
    iv = cipher_text[:DES3.block_size]  # Extract the IV from the beginning of the ciphertext
    cipher_text = cipher_text[DES3.block_size:]  # Extract the actual ciphertext
    cipher = DES3.new(key, DES3.MODE_CBC, iv)  # Recreate the cipher with the extracted IV
    decrypted_data = unpad(cipher.decrypt(cipher_text), DES3.block_size)  # Decrypt and unpad
    return decrypted_data.decode()  # Return the original plaintext

# Function to generate a secure 3DES key
def generate_key():
    return get_random_bytes(24)  # 3DES key must be 24 bytes

# Example usage
key = generate_key()
plain_text = "This is a secret message!"

# Encrypt the plaintext
cipher_text = encrypt_3des(plain_text, key)
print("Cipher Text (Hex):", binascii.hexlify(cipher_text))  # Convert to hex for readability

# Decrypt the ciphertext
decrypted_message = decrypt_3des(cipher_text, key)
print("Decrypted Message:", decrypted_message)
