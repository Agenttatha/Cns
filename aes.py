from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from secrets import token_bytes

def generate_key(key_size=32):
    return token_bytes(key_size)

def encrypt(plaintext, key):
    cipher = AES.new(key, AES.MODE_CBC)
    iv = cipher.iv
    padded_text = pad(plaintext.encode('utf-8'), AES.block_size)
    ciphertext = cipher.encrypt(padded_text)
    return iv + ciphertext

def decrypt(ciphertext, key):
    iv = ciphertext[:16]
    actual_ciphertext = ciphertext[16:]
    cipher = AES.new(key, AES.MODE_CBC, iv)
    decrypted_text = unpad(cipher.decrypt(actual_ciphertext), AES.block_size)
    return decrypted_text.decode('utf-8')

if __name__ == '__main__':
    key = generate_key(32)
    print("Key:", key.hex())

    plaintext = "HELLO AES"
    print("Original text:", plaintext)

    ciphertext = encrypt(plaintext, key)
    print("Encrypted text:", ciphertext.hex())

    decrypted_text = decrypt(ciphertext, key)
    print("Decrypted text:", decrypted_text)
