import cryptography
import getpass
from cryptography.fernet import Fernet

try:
    # load key file
    file = open('key.key', 'rb')
    key = file.read() # The key will be type bytes
    file.close()
    print("key.key file loaded successfully")

    # encrypt pwd
    pwd = getpass.getpass()
    f = Fernet(key)
    encrypted = f.encrypt(pwd)
    print "Encrypted pwd (to copy to config file): ", encrypted

    # decrypt msg
    decrypted = f.decrypt(encrypted)
    print(decrypted)

except:
    # generate key file if doesn't exists
    print("Error: key file does not exits, program will generate key.key")
    key = Fernet.generate_key()
    file = open('key.key', 'wb')
    file.write(key)
    file.close()
    print("key.key file generated successfully")



