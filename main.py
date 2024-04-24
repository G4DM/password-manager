# First of all, credits to Tech With Tim for teaching this project

# Modules

from cryptography.fernet import Fernet

master_password = input("What is the master password?: ")

def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)

# This password is used to encrypt the other passwords, even if the password typed is incorrect, it will still show the passwords,
# but encrypted. So the user still has access to the usernames and passwords, but these are encrypted so you need to have
# the master password to be able to access the passwords.

def add():
    name = input("Account name: ")
    pwd = input("Password: ")

    with open("passwords.txt", "a") as f:
        f.write(name + " | " + pwd + "\n")

def view():
    with open("passwords.txt", "r") as f:
        for line in f.readlines():
            data = line.rstrip()
            user, pwd = data.split(" | ")
            print(f"User: {user} | Password: {pwd}")

while True:
    mode = input("Would you like to add (add) a new password, view (view) existing ones or quit (q) the application?: ").lower()
    if mode == "q":
        break

    if mode == "add":
        add()
    elif mode == "view":
        view()
    else:
        print("Invalid mode.")
        continue