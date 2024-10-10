import random
import array
import csv
from os import read
import pandas

def gen_pwd():
    MAX_LEN = 12

    DIGITS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']  
    LOCASE_CHARACTERS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h','i', 'j', 'k', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y','z']

    UPCASE_CHARACTERS = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H','I', 'J', 'K', 'M', 'N', 'O', 'p', 'Q','R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y','Z']

    SYMBOLS = ['@', '#', '$', '%', '=', ':', '?', '.', '/', '|', '~', '>','*', '(', ')', '<']

    COMBINED_LIST = DIGITS + UPCASE_CHARACTERS + LOCASE_CHARACTERS + SYMBOLS

    rand_digit = random.choice(DIGITS)
    rand_upper = random.choice(UPCASE_CHARACTERS)
    rand_lower = random.choice(LOCASE_CHARACTERS)
    rand_symbol = random.choice(SYMBOLS)

    temp_pass = rand_digit + rand_upper + rand_lower + rand_symbol

    for x in range(MAX_LEN - 4):
        temp_pass = temp_pass + random.choice(COMBINED_LIST)
        temp_pass_list = array.array('u', temp_pass)
        random.shuffle(temp_pass_list)
        global g_pwd
        g_pwd= ""

        for x in temp_pass_list:
            g_pwd = g_pwd + x
    
    print("Password Generated successfully!!\n",g_pwd)

    clip_pwd = pandas.DataFrame([g_pwd])
    clip_pwd.to_clipboard(index=False, header=False)

    print("Copied to Clipboard!!")

def entryc():
    with open('data.csv', 'a') as cfile:
       entry = csv.DictWriter(cfile, fieldnames=['Website/Service', 'Username/Email-Id', 'Password'])
       while True:
            service = input("Enter the name of ````website/ service provider```:\n> ")
            user = input("Enter the ```username/ email-id``` by which the password is stored:\n> ")  

            n_choice = input("Suggest Password?(y/n) >").lower()

            if n_choice == 'y':
                gen_pwd()
                l_dict = {'Website/Service': service, 'Username/Email-Id': user, 'Password': g_pwd}
                entry.writerow(l_dict)
                print('Recorded Successfully!')

            if n_choice == 'n':
                pwd_1 = input("Enter the ```Password```:\n Double check the password then hit Return\n> ")
                pwd = input("Enter the ```Password``` again...\n> ")
                if pwd_1 == pwd:
                    l_dict = {'Website/Service': service, 'Username/Email-Id': user, 'Password': pwd}
                    entry.writerow(l_dict)
                    print('Recorded Successfully!')

                else:
                    print("The passowrds are not the same...\nThus not recorded...")

            elif n_choice != 'y' and n_choice != 'n':
                print("INVALID CHOICE!")
                print("Not Recorded...")               

            cont = input('Do you want to add another pwd?(y/n)').lower()
            if cont == 'n':
                print()
                break
            elif cont == 'y':
                pass
            
            else:
                print('INVALID OPTION!')
                break


def readc():

    print('_'*80)
    csv_data = pandas.read_csv('data.csv', names=['Website/Service', 'Username/Email-Id', 'Password'])
    print(csv_data)
    print('_'*80)



def searchc():
    
    query = input("Find(Not case sensitive):\n> ")
    with open('data.csv', 'r') as cfile:
        reader = csv.reader(cfile)
        for row in reader:
            for col in row:
                if col.lower() in query.lower():
                    print('|-------------------------------------------------------|')
                    print(f'Website/Service   : {row[0]}')
                    print(f'Username/Email-Id : {row[1]}')
                    print(f'Password          : {row[2]}')        
                    print('|-------------------------------------------------------|')
        
        
        
def deletec():
    try: 
        df = pandas.read_csv('data.csv', names=['Website/Service', 'Username/Email-Id', 'Password'])
        print(df)

        index_number = input("Enter the Index Number of Row to be deleted:\n> ")

        df = df.drop([int(index_number)])
        df.to_csv('data.csv', index=False, header=False)

        print("\nEdited Record: ")
        print(df)
    except ValueError:
        print('Not a number try again!')
        print("Nothing was deleted...")
        
        
if __name__ == '__main__': 
    entryc()
    readc()
    searchc()
    deletec()
