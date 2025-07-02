def check_balance(balance):
    print(f"Your balance is: ${balance}")

def deposit(balance, amount):
    if amount > 0:
        balance += amount
        print(f"${amount} deposited. New balance is: ${balance}")
    else:
        print("Deposit amount must be positive.")
    return balance

def withdraw(balance, amount):
    if amount > 0:
        if balance >= amount:
            balance -= amount
            print(f"${amount} withdrawn. New balance is: ${balance}")
        else:
            print("Insufficient balance.")
    else:
        print("Withdrawal amount must be positive.")
    return balance

def change_pin(current_pin):
    while True:
        old_pin = input("Enter your current PIN: ")
        if old_pin == current_pin:
            new_pin = input("Enter your new PIN: ")
            confirm_pin = input("Confirm your new PIN: ")
            if new_pin == confirm_pin:
                print("PIN successfully changed.")
                return new_pin
            else:
                print("New PIN and confirmation do not match. Try again.")
        else:
            print("Incorrect current PIN. Try again.")

def atm_menu():
    correct_pin = "1234"  # Set the initial correct PIN
    attempts = 3  # Number of allowed attempts
    balance = 100  # Initial balance

    while attempts > 0:
        entered_pin = input("Please enter your PIN: ")
        if entered_pin == correct_pin:
            print("PIN accepted.")
            while True:
                print("\nATM Menu:")
                print("1. Check Balance")
                print("2. Deposit Money")
                print("3. Withdraw Money")
                print("4. Change PIN")
                print("5. Exit")

                choice = input("Enter choice: ")

                if choice == '1':
                    check_balance(balance)
                elif choice == '2':
                    amount = float(input("Enter amount to deposit: "))
                    balance = deposit(balance, amount)
                elif choice == '3':
                    amount = float(input("Enter amount to withdraw: "))
                    balance = withdraw(balance, amount)
                elif choice == '4':
                    correct_pin = change_pin(correct_pin)
                elif choice == '5':
                    print("Thank you for using the ATM. Goodbye!")
                    return  # Exit the function to end the program
                else:
                    print("Invalid choice. Please try again.")
            break
        else:
            attempts -= 1
            print(f"Incorrect PIN. You have {attempts} attempt(s) remaining.")

    if attempts == 0:
        print("Too many incorrect attempts. Access denied.")

# Starting point
if input("Would you like to use the ATM? (yes/no): ").lower() == 'yes':
    atm_menu()
else:
    print("Goodbye!")
