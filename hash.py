import hashlib
import time

print("***Bank Verification***")
time.sleep(1)

name = input("Please enter your name \n")
hash_name4 = hashlib.sha256(name.encode())
hex_dig4 = hash_name4.hexdigest()

pin = input("Please enter your PIN\n")




x = input("Please enter your bank account number\n")
hash_name = hashlib.sha256(x.encode())
hex_dig = hash_name.hexdigest()

z = input("Please enter your SSN with no spaces or dashes \n")
hash_name2 = hashlib.sha256(z.encode())
hex_dig2 = hash_name2.hexdigest()

y = input("Please enter the amount to transfer\n")
hash_name3 = hashlib.sha256(y.encode())
hex_dig3 = hash_name3.hexdigest()




print(hex_dig)
print(hex_dig2)
print(hex_dig3)
print(hex_dig4)




