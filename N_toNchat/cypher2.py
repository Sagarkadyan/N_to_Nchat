from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad

key = b'mysecretaeskey12'  # Must be the same as sender's key

# Assume received_data = iv + ciphertext
received_data = ...  # Comes from websocket
iv = received_data[:16]
ciphertext = received_data[16:]

cipher = AES.new(key, AES.MODE_CBC, iv)
plaintext = unpad(cipher.decrypt(ciphertext), AES.block_size)
print(plaintext.decode())