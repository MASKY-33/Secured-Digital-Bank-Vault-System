from auth import check_balance, withdrawal_money


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
