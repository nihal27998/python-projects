pwd = input("Enter the master password: ")
def view():
    try:
        with open("password.txt","a") as f:
            for line in f:
                data = line.strip().split("|")
                print(f"Site:{data[0]},username.{data[1]},Passsword: {data[2]}")
    except FileNotFoundError:
        print("No saved password yet.")
def add():
    site = input("Enter th site: ")
    username = input("Enter the username: ")
    password = input("Enter the password: ")
    with open("passwords.txt","a") as f:
        f.write = (F"{site}|{username}|{password}\n")
while True:
    mode = input("Would you like to change the password or View the existing ones (view,add)? Press q to quit: ").lower()
    if mode =="q":
        break
    elif mode == 'add':
        add()
    else:
        print("Invalid Mode. ")
        continue