from cryptography.fernet import Fernet
from passlib.context import CryptContext
import pickle
from getpass import getpass

# intialisation of passlib
pwd_context = CryptContext(
        schemes=["pbkdf2_sha256"],
        default="pbkdf2_sha256",
        pbkdf2_sha256__default_rounds=30000
)

def gen_key():
   key = Fernet.generate_key()
   with open('filekey.key', 'wb') as filekey:
      filekey.write(key)
      print("Succesfully generated key!")
      print('\n')

def encrypt():
    with open('filekey.key', 'rb') as filekey:
        key = filekey.read()

    fernet = Fernet(key)

    with open('data.csv', 'rb') as file:
        original = file.read()

    encrypted = fernet.encrypt(original)

    with open('data.csv', 'wb') as encrypted_file:
        encrypted_file.write(encrypted)

def decrypt():
    with open('filekey.key', 'rb') as filekey:
        key = filekey.read()

    fernet = Fernet(key)

    with open('data.csv', 'rb') as enc_file:
        encrypted = enc_file.read()

    decrypted = fernet.decrypt(encrypted)

    with open('data.csv', 'wb') as dec_file:
        dec_file.write(decrypted)

def encrypt_password():
    pwd_d = input("Enter NEW Master Password\n> ")
    en_pwd = pwd_context.hash(pwd_d)
    with open('m_pwd.dat', 'wb') as pf:
        pickle.dump(en_pwd, pf)
    print("Sucessfully encoded new Master Password!")

def check_encrypted_password():
    pwd_d = getpass("Enter Master Password\n> ")
    pwd_e = bytes(pwd_d, 'utf-8')
    with open('m_pwd.dat', 'rb') as pf:
        hashed = pickle.load(pf)
    global check_pwd
    check_pwd = pwd_context.verify(pwd_e, hashed)


if __name__ == '__main__': 
    encrypt()
    decrypt()
    check_encrypted_password()
    encrypt_password()


