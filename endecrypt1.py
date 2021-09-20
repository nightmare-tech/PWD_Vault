from cryptography.fernet import Fernet

def gen_key():
   key = Fernet.generate_key()
   with open('filekey.key', 'wb') as filekey:
      filekey.write(key)
      print("Succesfully generated key!")
      print('\n')

