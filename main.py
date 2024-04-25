# First of all, credits to Tech With Tim for teaching this project

# Modules

from cryptography.fernet import Fernet

# This function was needed to create the key.key file

'''def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)'''

def load_key():
    file =  open("key.key", "rb")
    key = file.read()
    file.close()
    return key

key = load_key()
fer = Fernet(key)

def add():  
    name = input("Account name: ")
    pwd = input("Password: ")

    with open("passwords.txt", "a") as f:
        f.write(name + " | " + fer.encrypt(pwd.encode()).decode() + "\n")

def view():
    with open("passwords.txt", "r") as f:
        for line in f.readlines():
            data = line.rstrip()
            user, pwd = data.split(" | ")
            print(f"User: {user} | Password: {fer.decrypt(pwd.encode()).decode()}")

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