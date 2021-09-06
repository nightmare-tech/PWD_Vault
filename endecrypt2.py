from cryptography.fernet import Fernet

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

    

if __name__ == '__main__': 
    encrypt()
    decrypt()
