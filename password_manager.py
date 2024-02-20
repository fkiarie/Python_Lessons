master_pwd = input("Enter the master password")

def view():
    pass

def add():
    name = input("Account name: ")
    password = input("Password: ")

    with open("passwords.txt",'a') as f:
        f.write(name + " | " + password + "\n")

while True:
    mode = input("View or add new password? (view, add) press q for quit").lower()
    if mode == "q":
        break

    if mode == "view":
        view()
    elif mode == "add":
        add()
    else:
        print("Invalid input")
        continue