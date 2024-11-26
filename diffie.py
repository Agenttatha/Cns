import random

def power_mod(base, exponent, modulus):
    result = 1
    while exponent > 0:
        if exponent % 2 == 1:
            result = (result * base) % modulus
        base = (base * base) % modulus
        exponent //= 2
    return result

def diffie_hellman(p, g):
    print(f"Prime number (p): {p}")
    print(f"Base (g): {g}")
    
    # Alice's and Bob's private keys
    a = random.randint(2, p - 2)
    b = random.randint(2, p - 2)
    print(f"Alice's private key (a): {a}")
    print(f"Bob's private key (b): {b}")
    
    # Alice's and Bob's public values
    A = power_mod(g, a, p)
    print(f"Alice's public value (A = g^a mod p): {A}")
    B = power_mod(g, b, p)
    print(f"Bob's public value (B = g^b mod p): {B}")
    
    # Shared secret keys
    K_A = power_mod(B, a, p)
    print(f"Alice's shared secret key (K_A = B^a mod p): {K_A}")
    K_B = power_mod(A, b, p)
    print(f"Bob's shared secret key (K_B = A^b mod p): {K_B}")
    
    if K_A == K_B:
        print(f"Shared secret key: {K_A}")
    else:
        print("Something went wrong. The shared keys don't match!")

if __name__ == "__main__":
    p = 23  # Example prime number
    g = 5   # Example base
    diffie_hellman(p, g)



