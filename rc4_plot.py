import os
import time
import matplotlib.pyplot as plt

def rc4_encrypt_decrypt(key, data):
    S = list(range(256))
    j = 0

    # Key-Scheduling Algorithm (KSA)
    for i in range(256):
        j = (j + S[i] + key[i % len(key)]) % 256
        S[i], S[j] = S[j], S[i]

    # Pseudo-Random Generation Algorithm (PRGA)
    i = j = 0
    result = []
    for char in data:
        i = (i + 1) % 256
        j = (j + S[i]) % 256
        S[i], S[j] = S[j], S[i]
        result.append(char ^ S[(S[i] + S[j]) % 256])
    return bytes(result)

def create_random_file(filename, size_kb):
    with open(filename, "wb") as f:
        f.write(os.urandom(size_kb * 1024))

def read_file(filename):
    with open(filename, "rb") as f:
        return f.read()

def write_file(filename, data):
    with open(filename, "wb") as f:
        f.write(data)

def main():
    # Step 1: Create files
    file_sizes = [100, 500, 1000]  # Sizes in KB
    files = [f"file_{size}.bin" for size in file_sizes]

    for file, size in zip(files, file_sizes):
        create_random_file(file, size)

    # Step 2: Encrypt and Decrypt
    results = []
    key = b"securekey"
    for file in files:
        # Read plaintext
        plaintext = read_file(file)

        # Encrypt
        start_time = time.time()
        encrypted_data = rc4_encrypt_decrypt(key, plaintext)
        encryption_time = time.time() - start_time

        # Decrypt
        start_time = time.time()
        decrypted_data = rc4_encrypt_decrypt(key, encrypted_data)
        decryption_time = time.time() - start_time

        # Verify decryption
        assert plaintext == decrypted_data, "Decryption failed!"

        # Save results
        results.append({
            "file": file,
            "size_kb": len(plaintext) // 1024,
            "encryption_time": encryption_time,
            "decryption_time": decryption_time
        })

    # Step 3: Tabulate Results
    print(f"{'File':<15}{'Size (KB)':<10}{'Enc Time (s)':<15}{'Dec Time (s)':<15}")
    for result in results:
        print(f"{result['file']:<15}{result['size_kb']:<10}{result['encryption_time']:<15.5f}{result['decryption_time']:<15.5f}")

    # Step 4: Plot Results
    sizes = [result["size_kb"] for result in results]
    enc_times = [result["encryption_time"] for result in results]
    dec_times = [result["decryption_time"] for result in results]

    plt.plot(sizes, enc_times, label="Encryption Time")
    plt.plot(sizes, dec_times, label="Decryption Time")
    plt.xlabel("File Size (KB)")
    plt.ylabel("Time (s)")
    plt.title("RC4 Encryption and Decryption Time")
    plt.legend()
    plt.grid()
    plt.show()

if __name__ == "__main__":
    main()
