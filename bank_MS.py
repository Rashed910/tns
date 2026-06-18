# Dictionary to store bank account information

bank_database = {}


def create_account(account_number, customer_name, account_pin, opening_balance=0.0):
    """Create a new bank account."""

    # Check if account already exists
    if account_number in bank_database:
        print(f"Error: Account {account_number} already exists.")
        return False

    # Add account details to the database
    bank_database[account_number] = {
        "customer_name": customer_name,
        "account_pin": account_pin,
        "account_balance": opening_balance
    }

    print(f"Success: Account created for {customer_name}.")
    print(f"Starting Balance: ${opening_balance}")
    return True


def deposit_money(account_number, deposit_amount):
    """Deposit money into an account."""

    # Check if account exists
    if account_number not in bank_database:
        print(f"Error: Account {account_number} not found.")
        return False

    # Validate deposit amount
    if deposit_amount <= 0:
        print("Error: Deposit amount must be greater than zero.")
        return False

    # Add money to account balance
    bank_database[account_number]["account_balance"] += deposit_amount

    print(
        f"Success: Deposited ${deposit_amount}. New Balance: ${bank_database[account_number]['account_balance']}"
    )
    return True


def withdraw_money(account_number, entered_pin, withdrawal_amount):
    """Withdraw money from an account."""

    # Check if account exists
    if account_number not in bank_database:
        print(f"Error: Account {account_number} not found.")
        return False

    account_details = bank_database[account_number]

    # Verify PIN
    if account_details["account_pin"] != entered_pin:
        print("Error: Incorrect PIN.")
        return False

    # Check sufficient balance
    if withdrawal_amount > account_details["account_balance"]:
        print(
            f"Error: Insufficient funds. Current Balance: ${account_details['account_balance']}"
        )
        return False

    # Deduct money from balance
    account_details["account_balance"] -= withdrawal_amount

    print(
        f"Success: Withdrew ${withdrawal_amount}. New Balance: ${account_details['account_balance']}"
    )
    return True


def check_balance(account_number, entered_pin):
    """Display account balance."""

    # Check if account exists
    if account_number not in bank_database:
        print(f"Error: Account {account_number} not found.")
        return None

    account_details = bank_database[account_number]

    # Verify PIN
    if account_details["account_pin"] != entered_pin:
        print("Error: Incorrect PIN.")
        return None

    print("\n--- ACCOUNT DETAILS ---")
    print(f"Customer Name : {account_details['customer_name']}")
    print(f"Account Number: {account_number}")
    print(f"Balance       : ${account_details['account_balance']}")

    return account_details["account_balance"]


# ---------------- MAIN PROGRAM ---------------- #

print("===== SIMPLE BANK MANAGEMENT SYSTEM =====")

while True:
    print("\nChoose an Option:")
    print("1. Create Account")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Check Balance")
    print("5. Exit")

    user_choice = input("Enter your choice (1-5): ")

    if user_choice == "1":
        account_number = int(input("Enter Account Number: "))
        customer_name = input("Enter Customer Name: ")
        account_pin = int(input("Create a 4-digit PIN: "))
        opening_balance = float(input("Enter Initial Deposit: "))

        create_account(
            account_number,
            customer_name,
            account_pin,
            opening_balance
        )

    elif user_choice == "2":
        account_number = int(input("Enter Account Number: "))
        deposit_amount = float(input("Enter Deposit Amount: "))

        deposit_money(account_number, deposit_amount)

    elif user_choice == "3":
        account_number = int(input("Enter Account Number: "))
        entered_pin = int(input("Enter PIN: "))
        withdrawal_amount = float(input("Enter Withdrawal Amount: "))

        withdraw_money(
            account_number,
            entered_pin,
            withdrawal_amount
        )

    elif user_choice == "4":
        account_number = int(input("Enter Account Number: "))
        entered_pin = int(input("Enter PIN: "))

        check_balance(account_number, entered_pin)

    elif user_choice == "5":
        print("Thank you for using the Bank Management System.")
        break

    else:
        print("Invalid choice. Please try again.")