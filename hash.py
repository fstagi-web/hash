import hashlib

x = input("Please enter your bank account number\n")
hash_name = hashlib.sha256(x.encode())
hex_dig = hash_name.hexdigest()

z = input("Please enter your SSN with no spaces or dashes \n")
hash_name2 = hashlib.sha256(z.encode())
hex_dig2 = hash_name2.hexdigest()

print(hex_dig)
print(hex_dig2)






