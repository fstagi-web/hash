import hashlib

x = input("Please enter your bank account number\n")
hash_name = hashlib.sha512(x.encode())
hex_dig = hash_name.hexdigest()
print(hex_dig)