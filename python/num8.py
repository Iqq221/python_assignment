#Authentication: Ask username, password and compare with encryption
import hashlib
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()
stored_username="admin"
stored_password_hash=hash_password("12345")
uname=input("enter username- ")
passwrd=input("enter password- ")
passwrd_hash=hash_password(passwrd)
if(uname==stored_username and passwrd_hash==stored_password_hash):
    print("login successful")
else:
    print("invalid username or password")
