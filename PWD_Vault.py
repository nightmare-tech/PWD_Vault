import base64
from endecrypt2 import decrypt
from endecrypt2 import encrypt
from endecrypt1 import gen_key
from encoder import enco 
from maincsv import entryc
from maincsv import readc
from maincsv import searchc

def login_screen():

    print('|*****************WELCOME*******************|')
    print('|-------------------------------------------|')
    print('|----------------PWD_Vault                  |')
    print('|-------------------------------------------|')
    print('|----------Developed by Arpit Gupta         |')
    print('|-------------------------------------------|')
    print('|--------------LOGIN SCREEN                 |')
    print('|-------------------------------------------|')
    print('|----1. Enter the Master Password           |')
    print('|-------------------------------------------|')
    print('|-------------------------------------------|')
    print('|--s = First-Time-Setup (Only run this once)|')
    print('|You may not be able to acess your files if |')
    print('|if this is run again.                      |')
    print('|-------------------------------------------|')
    print('|-------------------------------------------|')    
    print('|----h = Help                               |')
    print('|----q = quit                               |')
    print('|-------------------------------------------|')
    print('|!!Do not use Ctrl + C to exit the program!!|')
    print('|!!always use the \'q\' option to exit    !!|')
    print('|-------------------------------------------|')
    print('|-------------------------------------------|')



    option = input('> ')
    if option == '1':
        with open('nothinghere.dat', 'rb') as bt_file:
            decodedBytes = bt_file.read()
            decodedStr = str(decodedBytes, 'utf-8')
                        
            decoded_pwd = base64.b64decode(decodedStr)
            str_pwd = decoded_pwd.decode()
            password = input('Enter Master Password:\n> ')

        if str_pwd == password:
            print('Login Success!')
            decrypt()
            main_menu()
        else: 
            print('Wrong Password')
            input("Press any key to return to the login screen...\n> ")
            login_screen()
          
    elif option == 's':
        print('\n')
        enco()
        print('\n')
        gen_key()
        print('Great! Now remeber the master passwrd that you encoded as it will not be provided again in future...')
        print("'Remember one Strong Password than a 100 weak ones...'")
        input("Press any key to go to the main menu...\n> ")
        main_menu()

    elif option == 'h':
        with open('help.txt', 'r') as manual:
            reader = manual.read()
            print(reader)
            print('\n')
            input("Press any key to return to the login screen...\n> ")
            login_screen()

    elif option == 'q':
            print("Exiting...")
            quit()
    else:
        print('Invalid Option')
        input("Press any key to return to the login screen...\n> ")
        login_screen()



def main_menu():
    print('|-------------------------------------------|')
    print('|-------------------------------------------|')
    print('|-----------------PWD_Vault                 |')
    print('|-------------------------------------------|')
    print('|-----------------MAIN MENU                 |')
    print('|-------------------------------------------|')
    print('|-------------------------------------------|')
    print('|-----1. Enter in Databse                   |')
    print('|-----2. Read all the stored data           |')
    print('|-----3. Search within all the stored data  |')
    print('|-------------------------------------------|')
    print('|-------------------------------------------|')
    print('|-------------------------------------------|')
    print('|h = Help                                   |')
    print('|-------------------------------------------|')
    print('|-------------------------------------------|')
    print('|-------------------------------------------|')
    print('|e = erase the file                         |')
    print('|q = quit                                   |')
    print('|-------------------------------------------|')
    print('|-------------------------------------------|')

    option = input('> ')
    if option == '1':
        print('\n')
        entryc()
        print('\n')
        input("Press any key to return to the main menu\n> ")
        main_menu()

    elif option == '2':
        print('\n')
        readc()
        print('\n')
        input("Press any key to return to the main menu\n> ")
        main_menu()

    elif option == '3':
        print('\n')
        searchc()
        print('\n')
        input("Press any key to return to the main menu\n> ")
        main_menu()

    elif option == 'h':
        print('\n')
        with open('help.txt', 'r') as manual:
            reader = manual.read()
            print(reader)
            input("Press any key to return to the main menu\n> ")
        print('\n')
        main_menu()

    elif option == 'e':
        print('Are you sure you that you want to erase the data?(y/n) ')
        sure = input('> ')
        if sure == 'y':
            with open('data.csv', 'w') as slaughter:
                slaughter.truncate()
                print('The data will never be found again!')
                input("Press any key to return to the main menu\n> ")
                main_menu()

        elif sure == 'n':
            print('No Problem')
            main_menu()
        else:
            print('\nINVALID OPTION')
            input("Press any key to return to the main menu\n> ")
            main_menu()
    
    elif option == 'q':
        print('Encrypting Data...')
        encrypt()
        print('Exiting...')
        quit()

    else:
        print('INVALID OPTION!')
        main_menu()




login_screen()


