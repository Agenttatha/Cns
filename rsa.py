import random
from math import gcd

# Function to compute modular inverse
def mod_inverse(e, phi):
    d = 0
    x1, x2, x3 = 1, 0, phi
    y1, y2, y3 = 0, 1, e
    while y3 != 1:
        q = x3 // y3
        t1, t2, t3 = x1 - q * y1, x2 - q * y2, x3 - q * y3
        x1, x2, x3 = y1, y2, y3
        y1, y2, y3 = t1, t2, t3
    return y2 % phi

# Function to perform modular exponentiation
def mod_exp(base, exp, mod):
    result = 1
    while exp > 0:
        if exp % 2 == 1:
            result = (result * base) % mod
        base = (base * base) % mod
        exp //= 2
    return result

# RSA Key Generation
def generate_keypair(p, q):
    n = p * q
    phi = (p - 1) * (q - 1)
    e = random.randrange(2, phi)
    while gcd(e, phi) != 1:
        e = random.randrange(2, phi)
    d = mod_inverse(e, phi)
    return ((e, n), (d, n))

# Encryption function
def encrypt(public_key, plaintext):
    e, n = public_key
    return [mod_exp(ord(char), e, n) for char in plaintext]

# Decryption function
def decrypt(private_key, ciphertext):
    d, n = private_key
    return ''.join([chr(mod_exp(char, d, n)) for char in ciphertext])

# Example usage
if __name__ == '__main__':
    p = 61
    q = 53
    public_key, private_key = generate_keypair(p, q)
    print("Public Key:", public_key)
    print("Private Key:", private_key)

    message = "HELLO"
    encrypted_msg = encrypt(public_key, message)
    print("Encrypted message:", encrypted_msg)

    decrypted_msg = decrypt(private_key, encrypted_msg)
    print("Decrypted message:", decrypted_msg)
