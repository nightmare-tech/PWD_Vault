import csv
from os import read
import pandas


def entryc():
    with open('data.csv', 'a') as cfile:
       entry = csv.DictWriter(cfile, fieldnames=['Website/Service', 'Username/Email-Id', 'Password'])
       while True:
            service = input("Enter the name of ````website/ service provider```:\n> ")
            user = input("Enter the ```username/ email-id``` by which the password is stored:\n> ")                
            pwd_1 = input("Enter the ```Password```:\n Double check the password then hit Return\n> ")
            pwd = input("Enter the ```Password``` again...\n> ")
            if pwd_1 == pwd:
                l_dict = {'Website/Service': service, 'Username/Email-Id': user, 'Password': pwd}
                entry.writerow(l_dict)
                print('Recorded Successfully')

            else:
                print("The passowrds are not the same...\nThus not recorded...")
                           

            cont = input('Do you want to add another pwd?(y/n)')
            if cont.lower() == 'n':
                print()
                break
            elif cont.lower() == 'y':
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
                    print('Website/Service   :',row[0])
                    print('Username/Email-Id :',row[1])
                    print('Password          :',row[2])        
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
