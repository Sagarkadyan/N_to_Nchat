from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad

message = "BSDK COPLOLET TE BHI CODE NA LIKGAVA NA GAYA"
key = get_random_bytes(16)  # AES-128
  # 16 bytes for CBC mode

# Encryption
cipher_encrypt = AES.new(key, AES.MODE_CBC, iv)
ciphertext = cipher_encrypt.encrypt(pad(message.encode(), AES.block_size))

# Decryption

print("Original message:", message)
print("Encrypted message:", ciphertext)
