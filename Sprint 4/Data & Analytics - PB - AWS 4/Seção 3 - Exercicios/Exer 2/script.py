import hashlib

while True:
    string = input("Digite uma string: ")
    sha1_hash = hashlib.sha1(string.encode()).hexdigest()
    print("Hash SHA-1: " + sha1_hash)
