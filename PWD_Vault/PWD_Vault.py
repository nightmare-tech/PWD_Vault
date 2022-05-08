import pickle
from passlib.context import CryptContext
from getpass import getpass
import endecrypt
from endecrypt import gen_key
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

def banner_p():
    fn_l = [one, two, three, four, five, six, seven, eight, ninne, ten, eleven, twelve, thirteen, fourteen, fifteen, sixteen, seventeen, eighteen, nineteen]
    random.choice(fn_l)()

def login_screen():
    try:

        print('|-------------------------------------------------------|')
        print('|--------------------LOGIN SCREEN ----------------------|')
        print('|-------------------------------------------------------|')
        print('|----1. Enter the Master Password ----------------------|')
        print('|-------------------------------------------------------|')
        print('|-------------------------------------------------------|')
        print('|-------------------------------------------------------|')
        print('|--s = First-Time-Setup (Only run this once) -----------|')
        print('|-------------------------------------------------------|')
        print('|-------------------------------------------------------|')    
        print('|----h = Help ------------------------------------------|')
        print('|----q = quit ------------------------------------------|')
        print('|-------------------------------------------------------|')
        print('\n')



        option = input('> ')
        if option == '1':
            check_encrypted_password()
            
            if endecrypt.check_pwd == True:
                print('Login Success!')
                decrypt()
                main_menu()
            else: 
                print('Wrong Password!!')
                login_screen()
            
        elif option == 's':
            print('\n')
            encrypt_password()
            print('\n')
            gen_key()
            print('Great! Now remeber the master passwrd that you encoded as it will not be provided again in future...')
            print("'Remember one Strong Password than a 100 weak ones...'")
            input("Hit Enter to go to the main menu...> ")
            main_menu()

        elif option == 'h':
            with open('help.txt', 'r') as manual:
                reader = manual.read()
                print(reader)
                print('\n')
                input("Hit Enter to return to the login screen...> ")
                login_screen()

        elif option == 'q':
                print("Exiting...")
                quit()

        elif option == 'banner':
            banner_p()
            login_screen()

        else:
            print('Invalid Option\n')
            login_screen()
            
    except FileNotFoundError:
        print('Run the first-time-setup first...')
        login_screen()
        


def main_menu():
    try:
        print('|-------------------------------------------------------|')
        print('|-------------------------------------------------------|')
        print('|-----------------------MAIN MENU ----------------------|')
        print('|-------------------------------------------------------|')
        print('|-------------------------------------------------------|')
        print('|-----1. Enter in Record -------------------------------|')
        print('|-----2. Read all the stored data ----------------------|')
        print('|-----3. Search within all the stored data -------------|')
        print('|-----4. Delete a record -------------------------------|')
        print('|-------------------------------------------------------|')
        print('|-------------------------------------------------------|')
        print('|h = Help ----------------------------------------------|')
        print('|-------------------------------------------------------|')
        print('|-------------------------------------------------------|')
        print('|-------------------------------------------------------|')
        print('|e = erase the file ------------------------------------|')
        print('|q = quit ----------------------------------------------|')
        print('|-------------------------------------------------------|')
        print('|-------------------------------------------------------|')

        option = input('> ')
        if option == '1':
            print('\n')
            entryc()
            print('\n')
            input("Hit Enter to return to the main menu\n> ")
            main_menu()

        elif option == '2':
            print('\n')
            readc()
            print('\n')
            input("Hit Enter to return to the main menu\n> ")
            main_menu()

        elif option == '3':
            print('\n')
            searchc()
            print('\n')
            input("Hit Enter to return to the main menu\n> ")
            main_menu()

        elif option =='4':
            print('\n')
            deletec()
            input("Hit Enter to return to the main menu\n> ")
            main_menu()

        elif option == 'h':
            print('\n')
            with open('help.txt', 'r') as manual:
                reader = manual.read()
                print(reader)
                input("Hit Enter to return to the main menu\n> ")
            print('\n')
            main_menu()

        elif option == 'e':
            print('Are you sure you that you want to erase the data?(y/n) ')
            sure = input('> ')
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
        
        elif option == 'q':
            print('Encrypting Data...')
            encrypt()
            print('Exiting...')
            quit()
        
        elif option == 'banner':
            banner_p()
            main_menu()
        else:
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
