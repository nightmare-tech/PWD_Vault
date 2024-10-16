import pickle
from passlib.context import CryptContext
from getpass import getpass
from endecrypt import encrypt
from endecrypt import decrypt
from endecrypt import encrypt_password
from endecrypt import check_encrypted_password
from maincsv import gen_pwd
from maincsv import entryc
from maincsv import readc
from maincsv import searchc
from maincsv import deletec
from banners import *
import random

global key

def is_file_empty(file_path):
    with open(file_path, 'r') as file:
        return file.read() == ''

def banner_p():
    fn_l = [one, two, three, four, five, six, seven, eight, nine, ten, eleven, twelve, thirteen, fourteen, fifteen, sixteen, seventeen, eighteen, nineteen]
    random.choice(fn_l)()

def login_screen():
    global key
    try:

        login_interface = """
        |-------------------------------------------------------|
        |--------------------LOGIN SCREEN ----------------------|
        |-------------------------------------------------------|
        |----1. Enter the Master Password-----------------------|
        |-------------------------------------------------------|
        |-------------------------------------------------------|
        |--s = First-Time-Setup (Only run this once) -----------|
        |-------------------------------------------------------|
        |-------------------------------------------------------|
        |-------------------------------------------------------|    
        |----h = Help ------------------------------------------|
        |----q = quit ------------------------------------------|
        |-------------------------------------------------------|
        """
        print (login_interface)

        option = input('> ')
        
        match option:
            case'1':
                key = check_encrypted_password()
            
                if key:  # If key is not None, login was successful
                    print('Login Success!')
                    decrypt(key)  
                    main_menu()
                else:
                    print('Wrong Password!!')
                    login_screen()
            
            case 's':
                print('Please Perform the First-time Set-up\n')
                key = encrypt_password()
                print('\n')
                print('Great! Now remember the master passwrd that you encoded as it will not be provided again in future...')
                print("'Remember one Strong Password than a 100 weak ones...'")
                input("Hit Enter to go to the main menu...> ")
                main_menu()

            case 'h':
                with open('PWD_Vault/PWD_Vault/help.txt', 'r') as manual:
                    reader = manual.read()
                    print(reader)
                    print('\n')
                    input("Hit Enter to return to the login screen...> ")
                    login_screen()

            case 'q':
                print("Exiting...")
                quit()

            case 'banner':
                banner_p()
                login_screen()

            case _:
                print('Invalid Option\n')
                login_screen()
            
    except FileNotFoundError:
        print('Run the first-time-setup first...')
        login_screen()
    except KeyboardInterrupt:
        print("\n!!!!!Use 'q' to exit!!!!")
        login_screen()
        


def main_menu():
    global key
    try:
        main_interface = """
        |-------------------------------------------------------|
        |-------------------------------------------------------|
        |-----------------------MAIN MENU ----------------------|
        |-------------------------------------------------------|
        |-------------------------------------------------------|
        |-----1. Enter in Record -------------------------------|
        |-----2. Read all the stored data ----------------------|
        |-----3. Search within all the stored data -------------|
        |-----4. Delete a record -------------------------------|
        |-------------------------------------------------------|
        |-------------------------------------------------------|
        |h = Help ----------------------------------------------|
        |-------------------------------------------------------|
        |-------------------------------------------------------|
        |-------------------------------------------------------|
        |e = erase the file ------------------------------------|
        |q = quit ----------------------------------------------|
        |-------------------------------------------------------|
        |-------------------------------------------------------|
        """
        print(main_interface)
        
        option = input('> ')
        
        match option:
            case '1':
                print('\n')
                entryc()
                print('\n')
                input("Hit Enter to return to the main menu\n> ")
                main_menu()

            case '2':
                print('\n')
                readc()
                print('\n')
                input("Hit Enter to return to the main menu\n> ")
                main_menu()

            case '3':
                print('\n')
                searchc()
                print('\n')
                input("Hit Enter to return to the main menu\n> ")
                main_menu()

            case '4':
                print('\n')
                deletec()
                input("Hit Enter to return to the main menu\n> ")
                main_menu()

            case 'h':
                print('\n')
                with open('PWD_Vault/PWD_Vault/help.txt', 'r') as manual:
                    reader = manual.read()
                    print(reader)
                    input("Hit Enter to return to the main menu\n> ")
                print('\n')
                main_menu()

            case 'e':
                print('Are you sure you that you want to erase the data?(y/n) ')
                sure = input('> ').lower()
                if sure == 'y':
                    with open('data.csv', 'w') as slaughter:
                        slaughter.truncate()
                        print('The data will never be found again!')
                        input("Hit Enter to return to the main menu\n> ")
                        main_menu()

                elif sure == 'n':
                    print('No Problem')
                    main_menu()
                else:
                    print('\nINVALID OPTION')
                    input("Hit Enter to return to the main menu\n> ")
                    main_menu()
        
            case 'q':
                print('Encrypting Data...')
                encrypt(key)
                print('Exiting...')
                quit()
        
            case 'banner':
                banner_p()
                main_menu()
                
            case _:
                print('INVALID OPTION!')
                main_menu()

    except KeyboardInterrupt:
        print("\n!!!!!Use 'q' to exit!!!!")
        main_menu()
   
# prevention of FileNotFoundError 
with open('data.csv', 'a') as db:
    pass   

banner_p()
login_screen()
