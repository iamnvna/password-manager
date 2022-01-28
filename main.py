from cryptography.fernet import Fernet

print("Welcome to Password Manager!")

'''
def write_key():
    keyfile = Fernet.generate_key()
    with open('key.key', 'wb') as f:
        f.write(keyfile)

write_key()
'''

def load_key():
    file = open('key.key', 'rb')
    keyfile = file.readline()
    file.close()
    return keyfile

key = load_key()
fer = Fernet(key)

def add():
    name = input("Enter account name: ")
    pwd = input("Enter account password: ")
    with open('passwords.txt', 'a') as f:
        f.write(name + "|" + fer.encrypt(pwd.encode()).decode() + "\n")

def view():
    with open('passwords.txt', 'r') as f:
        for line in f.readlines():
            data = line.rstrip()
            user, password = data.split("|")
            print("Account:", user, "Password:", fer.decrypt(password.encode()).decode())

while True:
    mode = input("Enter 'add' to add a password, 'view' to display passwords, and 'q' to quit: ").lower()
    if mode == 'q':
        break
    
    if mode == 'add':
        add()
    elif mode == 'view':
        view()
    else:
        print("Enter a valid input!")
        continue
