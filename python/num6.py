# Authentication: Ask username, password and compare
stored_username="admin"
stored_password="12345"
uname=input("enter username- ")
passwrd=input("enter password- ")
if(uname==stored_username and passwrd==stored_password):
    print("login successful")
else:
    print("invalid username or password")