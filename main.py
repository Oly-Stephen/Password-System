# New global variables
users = {}  # Dictionary to store user accounts and passwords
password_history = {}  # Dictionary to store password history


def create_password():
    while True:
        password = input("Create a new password: ")
        confirm_password = input("Confirm your password: ")
        if password == confirm_password:
            print("\n    ✅ Password created successfully!!! ✅    \n")
            return password
        else:
            print("❌ Passwords do not match. Please try again. ❌")


def create_account():
    username = input("Enter your desired username: ")
    while True:
        if username in users:
            print("❌ Username already exists. Please choose a different username. ❌")
            username = input("Enter your desired username: ")
        else:
            break

    password = create_password()
    users[username] = password
    password_history[username] = [password]  # Add initial password to history

    login_prompt = input("Account created successfully! Do you want to log in now? (yes/no): ")
    if login_prompt.lower() == "yes":
        login()


def change_password():
    while True:
        current_password = input("Enter your current password: ")
        if current_password == users[username]:
            new_password = create_password()
            password_history[username].append(new_password)  # Add new password to history
            users[username] = new_password
            return new_password
        else:
            print("❌ Incorrect password. Please try again. ❌")


def login():
    while True:
        entered_username = input("Enter your username: ")
        entered_password = input("Enter your password to log in: ")
        if entered_username in users and entered_password == users[entered_username]:
            print("\n    ✨✨✨ Access granted!    ✨✨✨\n"
                  "\n"
                  "    ----- LOGGED IN SUCCESSFULLY -----    \n")
            global username
            username = entered_username
            break
        else:
            print("\n    ❌ Incorrect username or password. Please try again.    \n❌")
            create_account_prompt = input("Create an account or login? (yes/no): ")
            if create_account_prompt.lower() == "yes":
                create_account()
            else:
                quit()

    change_prompt = input("Do you want to change your password? (yes/no): ")
    if change_prompt.lower() == "yes":
        password = change_password()


# Main program
while True:
    create_login = input("Create an account or login? (create/login): ")
    if create_login.lower() == "create":
        create_account()
        break
    elif create_login.lower() == "login":
        login()
        break
    else:
        print("❌ Invalid input. Please enter 'create' or 'login'. ❌")
