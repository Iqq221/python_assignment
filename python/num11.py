from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
key = b'ThisIsASecretKey'  # 16 bytes
cipher = AES.new(key, AES.MODE_ECB)
stored_username = "admin"
password_plain = "12345"
stored_password_encrypted = cipher.encrypt(pad(password_plain.encode(), AES.block_size))
username = input("Enter username: ")
password = input("Enter password: ")
entered_password_encrypted = cipher.encrypt(pad(password.encode(), AES.block_size))
if username == stored_username and entered_password_encrypted == stored_password_encrypted:
    print("Authentication successful!")
else:
    print("Authentication failed!")
