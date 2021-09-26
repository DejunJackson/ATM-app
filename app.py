from banking_pkg import account


def atm_menu(name):
    print("")
    print("          === Automated Teller Machine ===          ")
    print("User: " + name)
    print("------------------------------------------")
    print("| 1.    Balance     | 2.    Deposit      |")
    print("------------------------------------------")
    print("------------------------------------------")
    print("| 3.    Withdraw    | 4.    Logout       |")
    print("------------------------------------------")


print("          === Automated Teller Machine ===          ")
name = input("Enter your name to register: ")
balance = float(0)

while True:
    if len(name) < 1:
        print("Enter a name.")
        name = account.register_name()

    elif len(name) > 10:
        print("The max name length is 10 characters.")
        name = account.register_name()

    else:
        pin = input("Enter PIN: ")

        if len(pin) < 4 or len(pin) > 4:
            print("PIN must contain 4 numbers.")

        else:
            print(f'{name} has been registered with a starting balance of ${balance}')
            break

while True:
    print("          === Automated Teller Machine ===          ")
    print("LOGIN")
    name_to_validate = input("Enter name: ")
    pin_to_validate = input("Enter PIN: ")
    if name_to_validate == name and pin_to_validate == pin:
        print("Login successful!")
        break
    else:
        print("Invalid credentials!")

while True:
    atm_menu(name)
    option = input("Choose an option: ")
    if option == "1":
        account.show_balance(balance)
    elif option == "2":
        balance = account.deposit(balance)
        print(f"Current Balance: {balance}")
    elif option == "3":
        balance = account.withdraw(balance)
        print(f"Current Balance: {balance}")
    elif option == "4":
        account.logout(name)
        break
