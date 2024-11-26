import hashlib
def md5_hash(input_string):
    md5 = hashlib.md5()
    md5.update(input_string.encode('utf-8'))
    return md5.hexdigest()

input_string = "hello world"
print(f"Input: {input_string}")
print(f"MD5 Hash: {md5_hash(input_string)}")