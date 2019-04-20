import os
import cryptography
import getpass
from cryptography.fernet import Fernet

def encrypt_string(key):
    pwd = getpass.getpass()
    f = Fernet(key)
    encrypted = f.encrypt(pwd)
    print "Encrypted pwd (to copy to config file): ", encrypted

if os.path.exists("key.key"):
    # load key file
    file = open('key.key', 'rb')
    key = file.read() # The key will be type bytes
    file.close()
    print("key.key file loaded successfully")

    # encrypt pwd
    encrypt_string(key)

else:
    # generate key file if doesn't exists
    print("Error: key file does not exits, program will generate key.key")
    key = Fernet.generate_key()
    file = open('key.key', 'wb')
    file.write(key)
    file.close()
    print("key.key file generated successfully")

    # encrypt pwd
    encrypt_string(key)