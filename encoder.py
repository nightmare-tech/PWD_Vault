import base64
def enco():
        
    print("Always perform this in privacy!!\n Ensure then hit Enter...")
    input('>')

    pw = input("Enter new master password to be encoded (Case Sensitive)...\n> ")

    encodedBytes = base64.b64encode(pw.encode("utf-8"))
    encodedStr = str(encodedBytes, "utf-8")


    with open('nothinghere.dat', 'wb') as pw_file:
        pw_file.write(encodedBytes)
        
    print("Sucessfully encoded new Master Password!")

if __name__ == '__main__': 
    enco()