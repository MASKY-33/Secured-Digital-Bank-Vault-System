# My first (high-intermediate-level-system) using 2 Functions, and using try...except inside the functions.
# Inside the while-loop using 3 options to chose what requestions the user wants.


bank_accounts = {
    1001 : 500.00,
    1003 : 150.50,
    1005 : 75.00
}

def check_balance(account_id):

    try:
        numbers = int(account_id)

        if numbers in bank_accounts:
            return f"Balance: {bank_accounts[numbers]}"
        else:
            return "ID unknown."
        
    except ValueError:
        return "Login-ID must be numbers!"


def withdrawal_money(account_id, amount):

    try:
        numbers = int(account_id)
        floating = float(amount)
            
        if numbers in bank_accounts:
                
            check_amount = bank_accounts[numbers]
                
            if floating <= check_amount:
                bank_accounts[numbers] -= floating
                return f"Withdrawal successful! New balance: {bank_accounts[numbers]}"
            else:
                return "Insufficient balance."
        else:
            return "ID unkown."
            
    except ValueError:
        return "Error: Login-ID and/or withdrawing must be numbers!"


while True:
    print("\n--- Welcome at you Digitak Bank-Vault! ---")
    print("1. View balance")
    print("2; Withdrawal money")
    print("3. Close.")


    choice = input("Choose option (1-3): ")


    if choice == "3" or choice.lower() == "stop":
        print("Thankyou, Bye!")
        break


    elif choice == "1":
        id_request = input("Give in your login-ID: ")

        id_check = check_balance(id_request)
        print(id_check)


    elif choice == "2":
        id_request = input("Give in your login-ID: ")
        amount_request = input("How much money do you want to withdraw?: ")

        balance_check = withdrawal_money(id_request, amount_request)
        print(balance_check)

    else:
        print("Invalid choice, try again!")
