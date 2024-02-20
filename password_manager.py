pwd = input("Enter the master password")

while True:
    mode = input("View or add new password? (view, add) press q for quit").lower()
    if mode == "q":
        break

    if mode == "view":
        pass
    elif mode == "add":
        pass
    else:
        print("Invalid input")
        continue