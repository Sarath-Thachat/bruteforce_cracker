import hashlib

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

print("Create test password")
pwd = input("Enter password: ")

hashed = hash_password(pwd)

with open("hashes.txt", "w") as f:
    f.write(hashed)

print("\nStored SHA256 hash:")
print(hashed)
