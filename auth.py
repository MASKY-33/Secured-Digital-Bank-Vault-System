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
