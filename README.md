# PWD_Vault

PWD_Vault is a versatile everyday use password manager tool.

This program uses encryption to store your password, which can only be decrypted and viewed within the program.

# Table of Contents
- [Installation](#installation)
- [Run Locally](#run-locally)
- [Features](#features)
  
# Installation:
Download the zip via `github.com/nightmare-tech/PWD_Vault` or clone it via git :-
```
git clone https://nightmare-tech/PWD_Vault
```
It is a very small repository. So, I didn't need another way to install it. And it’s the easiest :)

# Run Locally:
### Create a virtual env so that it does not break default lib versions 
```
cd PWD_Vault
python -m venv .
source bin/activate
```
!!!  Install the necessary packages !!!

```
pip install -r requirements.txt
```

- For Windows users:
    Click on the batch file `PWD_Vault.bat` from your file manager or execute the batch file by typing
    `PWD_Vault.bat` in your console in the cloned directory (Windows Terminal, cmd etc.) 
    
- For Linux users:
    Make the bash script executable (only need to do one time) :-
    ```
    chmod +x PWD_Vault.sh
    ```
    Then running the bash script:-
    ```
    ./PWD_Vault.sh
    ```

- Alternative: 
  Run the python file `PWD_Vault.py` in the directory `PWD_Vault` directly:-
  ```
  cd PWD_Vault
  python3 PWD_Vault.py
  ```
    This is what the .bat and .sh scripts do. It just looks neat this way :)

# Features:

## Login Screen:
This menu has 4 options:

- **1. Enter the Master Password**:
    Prompts user for the Master Password to decrypt the data and to go to the main menu.

- **s = First-Time-Setup**:
    This prompts user to make a Master Password and encodes it and generates an encryption key
    !! Do not ever run this after you have run it once....!!
    !!This will not allow you to decrypt the data ever again!!

- **h = Help**:
    This brings you here O:)

- **q = quit**:
    Exits from the Program

## Main Menu:
The menu has 6 options:

- **1. Enter in Record**:
    This makes the user enter their strong passwords or use a suggested 15-character password which they don't need to remember.
    ! Just double check all the details or you would have to erase the whole file and start over !

- **2. Read all the stored data**:
    This prints out all the passwords with their details.

- **3. Search within all stored data**:
    Feeling lazy?
    This option lets you search for a specific keyword from all the details and then it prints out the rest of the details with the details. Fancy right?

- **4. Delete a record**:
    Let's you delete a record.
    !!!!However, you should input here only what you're asked for and the spelling must be correct otherwise it could deleta unwanted records!!!!

- **h = Help**:
    This brought you here. O:)

- **e = Erase the file**:
    Just in case you need to erase the contents of the file.

- **q = quit**:
    Encrypts the data and quits the program:)

- **banner**: Enter in Login Screen or Main Menu to print a stunning ascii art banner.


# Happy Encryption!!

