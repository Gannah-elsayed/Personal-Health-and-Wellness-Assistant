import hashlib
from tkinter import *

print("Please click the sign-up button to assign your data.\n")
def signup():
    file = open('myfile.txt', 'w')
    email = input("Enter your email: ")
    pwd = input("Enter your password: ")
    conf_pwd = input("Enter your confirm password: ")
    file.write(email + '\n')
    file.write(pwd + '\n')
    file.write(conf_pwd + '\n')
    file.close()
    if conf_pwd == pwd:
        enc = conf_pwd.encode()
        hash1 = hashlib.md5(enc).hexdigest()
        with open("myFile.txt", "w") as f:
            f.write(email + "\n")
            f.write(hash1)

        print("\t\t\t\t\t\t\tYou have registered successfully!\n")
        print("Please click the login button to access your profile.\n")
    else:
        print("Password is not the same as above!\n")
        conf_pwd = input("Try again, enter your confirm password: ")


def login():
    print("Please click the login button to access your profile.\n")
    email = input("Enter your email: ")
    pwd = input("Enter your password: ")
    auth = pwd.encode()
    auth_hash = hashlib.md5(auth).hexdigest()

    with open("myFile.txt", "r") as f:
        stored_email, stored_pwd = f.read().split("\n")

    if email == stored_email and auth_hash == stored_pwd:
        print("\t\t\t\t\t\t\tLogged in Successfully!")
    else:
        print("Login failed!")

root = Tk()
root.title("Sign Up/Login")

# Create labels and entry fields for user details
Label(root, text="Email").grid(row=0, column=0, padx=10, pady=5)
entry_email = Entry(root)
entry_email.grid(row=0, column=1, padx=10, pady=5)

Label(root, text="Password").grid(row=1, column=0, padx=10, pady=5)
entry_password = Entry(root, show="*")
entry_password.grid(row=1, column=1, padx=10, pady=5)

Label(root, text="Confirm Password").grid(row=2, column=0, padx=10, pady=5)
entry_confirm_password = Entry(root, show="*")
entry_confirm_password.grid(row=2, column=1, padx=10, pady=5)

# Create sign-up and login buttons
Button(root, text="Sign Up", command=signup).grid(row=3, column=0, padx=10, pady=5)
Button(root, text="Login", command=login).grid(row=3, column=1, padx=10, pady=5)

# Run the main event loop
root.mainloop()
#
# while True:
#     print("********** Login System **********")
#     print("1. Signup")
#     print("2. Login")
#     print("3. Exit")
#     ch = int(input("Enter your choice: "))
#
#     if ch == 1:
#         signup()
#     elif ch == 2:
#         login()
#     elif ch == 3:
#         break
#     else:
#         print("Wrong Choice!")