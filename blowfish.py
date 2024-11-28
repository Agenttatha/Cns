from Crypto.Cipher import Blowfish
from Crypto.Util.Padding import pad, unpad
from secrets import token_bytes

def generate_key():
    return token_bytes(16) 

def encrypt(plaintext, key):
    cipher = Blowfish.new(key, Blowfish.MODE_ECB) 
    padded_text = pad(plaintext.encode('utf-8'), Blowfish.block_size) 
    ciphertext = cipher.encrypt(padded_text) 
    return ciphertext

def decrypt(ciphertext, key):
    cipher = Blowfish.new(key, Blowfish.MODE_ECB)
    decrypted_text = unpad(cipher.decrypt(ciphertext), Blowfish.block_size)  
    return decrypted_text.decode('utf-8')

if __name__ == '__main__':
    key = generate_key()
    print("Key:", key.hex())

    plaintext = "HELLO BLOWFISH"
    print("Original text:", plaintext)

    ciphertext = encrypt(plaintext, key)
    print("Encrypted text:", ciphertext.hex())

    decrypted_text = decrypt(ciphertext, key)
    print("Decrypted text:", decrypted_text)
