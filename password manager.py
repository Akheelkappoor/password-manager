from cryptography.fernet import Fernet

'''
def write_key():
    key = Fernet.generate_key()
    with open("key.key","wb") as key_file:
        key_file.write(key)
'''

def open_key():
    with open("key.key","rb") as file:
        key = file.read()
        return key 
    
key = open_key()
fer = Fernet(key)  

def add():
    name = input("Account Name: ")
    pwd = input("password: ")
    
    with open("password.txt","a") as f:
        f.write(name + "|" + fer.encrypt(pwd.encode()).decode() + "\n") 
    
def view():
    with open("password.txt","r") as f:
        for line in f.readlines():
            read = line.rstrip()
            user,paswd = read.split("|")
            print("user:",user," ","password:", fer.decrypt(paswd.encode()).decode())
              
    
while True:
    
    mode = input("would you like to add a new password or view a exisiting one? type q for quit: ").lower() 
    
    if mode == "q":
        break
    if mode == "add":
        add()
    elif mode == "view":
        view()
    else:
        print("Invalid mode.")
        continue
