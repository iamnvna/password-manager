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


# Commentary
'''
Line 1:
    Line 1 is the python library that allows us to decrypt and encrypt the passwords that are stored in the
    password file created by the program. To install the 'crytography' library from which we imported Fernet
    use the 'pip install cryptography' cmd command.

Line 3:
    As has become a habit, line 3 is a simple print statement that welcomes users to the application.
    
Line 5-12:
    The block of code between line 5 and 12 is commented out because we intend to run it once, which we already
    have. The code is defined function, 'write_key' which generates a key pair that is used in the encryption
    and decryption of the passwords in the file. The keyfile variable is created to hold the key generated (Line 7).
    A new file key.key is created and opened with the 'with' keyword. The generated key from line 7 is written in
    the file as a byte character. For this function to run, it is called in line 11, which is also commented out
    after the first run.

Line 14-20:
    This block of code is a function that loads the key anytime the program runs. The loaded key is used to
    either encrypt new additions to the passwords.txt file or decrypt the existing ones should the user want
    to view their password database. The function returns the key anytime it is called (Line 20)

Line 21:
    The loaded key from line 20, which is held in the 'key' variable is passed to the Fernet library and used
    in the subsequent code.

Line 23-27:
    This block of code is a function that allows users to add a new username and password to the passwords.txt
    file. When called, it collects the username and password to be appended to the textfile and writes them to
    the file. It beforehand, the password is encoded as bytes before encrypted using the key from line 21. The
    encoded, encrypted password is however decoded afterwards to string to be able to concatenate it with the username
    string collected alongside it, and written to the passwords.txt file.

Line 29-34:
    This block of code is a function that reads the encrypted file in the passwords.txt file, and prints the
    output to the screen. Note the difference between where the .decode() method is placed in the view function
    and add function. The add function has the view code attached to the very end of the decrypted file to
    decode it as a string. The view function however has to decode the string before it is encrypted.

Line 36-47:
    The code before this block of code essentially do not do much since they are mostly functions which are called
    from these lines of code. The user is prompted to enter an input in line 37, add to add a new username and password,
    view to print to screen the existing ones, and q to quit the program. The user input is evaluated against the if
    statements in line 38-47 and the appropriate block of code is executed. Note that the while True conditional
    statement that precedes the block of code allows the program to run again automatically or quit depending on the
    'break' or 'continue' keywords.
'''