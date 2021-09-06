import csv
import pandas


def entryc():
    with open('data.csv', 'a') as cfile:
        fields = ['Website/Service', 'Name of User', 'Username/Email-Id', 'Password']
        entry = csv.DictWriter(cfile, fieldnames= fields)

        while True:
            service = input("Enter the name of website/ service provider:\n> ")
            name = input("Enter your name:\n> ")
            user = input("Enter the username/ email-id by which the password is stored:\n> ")                
            pwd_1 = input("Enter the password:\n Double check the password then hit Return\n> ")
            pwd = input("Enter the Password again...\n>")
            if pwd_1 == pwd:
                l_dict = {'Website/Service': service, 'Name of User': name, 'Username/Email-Id': user, 'Password': pwd}
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
    # table = Table(title='Passwords')

    # table.add_column('Website/Serivce', justify='right', style='green', no_wrap=True)
    # table.add_column('Username/Email-Id', style='cyan')
    # table.add_column('Detail Category')
    # table.add_column('Password', style='red')

    print('_'*80)
    csv_data = pandas.read_csv('data.csv', names=['Website/Service', 'Name of User', 'Username/Email-Id', 'Password'])
    print(csv_data)
    print('_'*80)



def searchc():
    count = 1
    items = []
    with open('data.csv', 'r') as cfile:
        reader = csv.reader(cfile)
        for rows in reader:
            items.append(rows)
        
    query = input("Find(Not case sensitive):\n> ")

    for item in items:

        if query.lower() in str(item).lower():
            print('_'*20)
            print(count, '.')
            print('Website/Serice:', item[0])
            print('Name of User:', item[1])
            print('Username/Email-Id:', item[2])
            print('Password:', item[3])
            print('_'*20)
            count += 1

    print(':'* 80)   
    


if __name__ == '__main__': 
    entryc()
    readc()
    searchc()