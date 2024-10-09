import os
import base64
import cryptography
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.backends import default_backend
from cryptography.fernet import Fernet
from passlib.context import CryptContext
import pickle
from getpass import getpass

PBKDF2_ITERATIONS = 100000

# intialisation of passlib
pwd_context = CryptContext(
        schemes=["pbkdf2_sha256"],
        default="pbkdf2_sha256",
        pbkdf2_sha256__default_rounds=30000
)

def B_PBKDF2(data, salt):
    backend = default_backend()
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=PBKDF2_ITERATIONS,
        backend=backend
    )
    
    return base64.urlsafe_b64encode(kdf.derive(data))

def PBKDF2(data, salt):
    return B_PBKDF2(data.encode('utf-8'), salt)

def encrypt(key):
    fernet = Fernet(key)

    with open('PWD_Vault/PWD_Vault/data.csv', 'rb') as file:
        original = file.read()

    encrypted = fernet.encrypt(original)

    with open('PWD_Vault/PWD_Vault/data.csv', 'wb') as encrypted_file:
        encrypted_file.write(encrypted)

def decrypt(key):
    fernet = Fernet(key)

 
        
def decrypt_data(key):
    try:
        fernet = Fernet(key)
        with open('PWD_Vault/PWD_Vault/data.csv', 'rb') as enc_file:
            encrypted = enc_file.read()

        decrypted = fernet.decrypt(encrypted)
        return decrypted
    except cryptography.fernet.InvalidToken:
        print("Decryption failed: Invalid token or incorrect key.")
        return None


def encrypt_password():
    salt = os.urandom(16)
    
    with open('PWD_Vault/PWD_Vault/salt.dat', 'wb') as f:
        f.write(salt)
       
    pwd_d = input("Enter NEW Master Password\n> ")
    key = PBKDF2(pwd_d, salt)
    en_pwd = B_PBKDF2(key, salt)
    with open('PWD_Vault/PWD_Vault/m_pwd.dat', 'wb') as pf:
        pickle.dump(en_pwd, pf)
    print("Sucessfully encoded new Master Password!")
    return key

def check_encrypted_password():
    salt = b""
    with open('PWD_Vault/PWD_Vault/salt.dat', 'rb') as f:
        salt = f.read()
      
    pwd_d = getpass("Enter Master Password\n> ")
    try:
        with open('PWD_Vault/PWD_Vault/m_pwd.dat', 'rb') as pf:
            hashed = pickle.load(pf)
        global check_pwd
        key = PBKDF2(pwd_d, salt)
        en_pwd = B_PBKDF2(key, salt)
        check_pwd = (en_pwd == hashed)
        return key

    except EOFError as e:
        print(f"Master Key Emprty")

if __name__ == '__main__': 
    encrypt()
    decrypt()
    check_encrypted_password()
    encrypt_password()


