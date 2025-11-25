def login(prefilled_account_ID=None, accounts=None):
    import bank_system
    if accounts is None:
        accounts = bank_system.accounts
    print("Welcome to the login page")
    if prefilled_account_ID:
        print(f"Using account ID shown at creation: {prefilled_account_ID}")
        if prefilled_account_ID in accounts:
            account_ID = prefilled_account_ID
        else:
            print("Prefilled account ID not found in bank records.")
            account_ID = input("Enter your account ID: ")
    else:
        account_ID = input("Enter your account ID: ")
    try:
        Pin = int(input("Enter your 4-digit PIN: "))
    except ValueError:
        print("Invalid PIN format.")
        return None
    if account_ID in accounts:
        if accounts[account_ID]['Pin'] == Pin:
            print("Login successful!")
            import menu
            menu.menu(account_ID, accounts)
            return account_ID
        else:
            print("Incorrect PIN.")
    else:
        print("Account ID not found.")
    return None
