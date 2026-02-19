import hashlib
import time
import itertools
import string
import sys

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()


# load target hash
with open("hashes.txt") as f:
    target_hash = f.read().strip()

start = time.time()

chars = string.ascii_lowercase + string.digits

for length in range(1,7):
    for guess in itertools.product(chars, repeat=length):
        guess = ''.join(guess)
        test_hash = hash_password(guess)

        if test_hash == target_hash:
            print("\n FOUND (bruteforce):", guess)
            break

end = time.time()
print(f"\nTime taken: {end - start:.2f} seconds")
sys.exit()