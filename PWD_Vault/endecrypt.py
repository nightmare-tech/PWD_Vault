import os
import base64
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.backends import default_backend
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

def gen_key(pwd):
    # don't touch my trash
    backend = default_backend()
    salt = b"1337"
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100000,
        backend=backend
    )
    
    return base64.urlsafe_b64encode(kdf.derive(pwd.encode('utf-8')))

def encrypt(key):
    fernet = Fernet(key)

    with open('data.csv', 'rb') as file:
        original = file.read()

    encrypted = fernet.encrypt(original)

    with open('data.csv', 'wb') as encrypted_file:
        encrypted_file.write(encrypted)

def decrypt(key):
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
    return pwd_d

def check_encrypted_password():
    pwd_d = getpass("Enter Master Password\n> ")
    pwd_e = bytes(pwd_d, 'utf-8')
    with open('m_pwd.dat', 'rb') as pf:
        hashed = pickle.load(pf)
    global check_pwd
    check_pwd = pwd_context.verify(pwd_e, hashed)
    return pwd_d


if __name__ == '__main__': 
    encrypt()
    decrypt()
    check_encrypted_password()
    encrypt_password()


