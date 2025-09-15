from cryptography.fernet import Fernet

key = Fernet.generate_key()
cipher = Fernet(key)

stored_username = "admin"
stored_password_encrypted = cipher.encrypt("12345".encode())

username = input("Enter username: ")
password = input("Enter password: ")

stored_password = cipher.decrypt(stored_password_encrypted).decode()

if username == stored_username and password == stored_password:
    print("Authentication successful!")
else:
    print("Authentication failed!")
