import hashlib
def sha1_hash(input_string):
    sha1 = hashlib.sha1()
    sha1.update(input_string.encode('utf-8'))
    return sha1.hexdigest()


input_string = "hello world"
print(f"Input: {input_string}")
print(f"SHA-1 Hash: {sha1_hash(input_string)}")