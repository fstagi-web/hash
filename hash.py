import hashlib
import time
import uuid

print("--------------")
print("**Bank Verification**")
print("--------------")
time.sleep(1)


# User Name

name = input("Please enter your name \n")
hash_name4 = hashlib.sha256(name.encode())
hex_dig4 = hash_name4.hexdigest()

#User Pin

pin = input("Please enter your PIN\n")
hash_name5 = hashlib.sha256(pin.encode())
hex_digi5 = hash_name5.hexdigest()


#User Acct Number

x = input("Please enter your bank account number\n")
hash_name = hashlib.sha256(x.encode())
hex_dig = hash_name.hexdigest()

#User SSN

z = input("Please enter your SSN with no spaces or dashes \n")
hash_name2 = hashlib.sha256(z.encode())
hex_dig2 = hash_name2.hexdigest()


#User Withdrawl amount

y = input("Please enter the amount to withdrawl\n")
hash_name3 = hashlib.sha256(y.encode())
hex_dig3 = hash_name3.hexdigest()

time.sleep(2)


print("---------------")
print("*TRANSACTION ID*", uuid.uuid4().hex[:8])
print("---------------")

time.sleep(1)

print("*NAME*:", hex_dig4)
print("*SSN*:", hex_dig2)
print("*BANK ACCOUNT NUMBER*:", hex_dig)
print("*PIN*:", hex_digi5)
print("*TRANSFER AMOUNT*:", hex_dig3)







