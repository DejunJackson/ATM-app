def show_balance(balance):
    print(f"Your account balance is: {balance}.")


def deposit(balance):
    amount = float(input("Enter amount to deposit: "))
    return amount + balance


def withdraw(balance):
    amount = float(input("Enter amount to withdraw: "))
    new_balance = balance - amount
    if new_balance < 0:
        print("You don't have that much in your account.")
        return balance
    else:
        return new_balance


def logout(name):
    print(f"Bye {name}")


def register_name():
    name = input("Enter your name to register: ")
    return name
