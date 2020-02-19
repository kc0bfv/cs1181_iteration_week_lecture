import payment

def pay():
    print("Ways to pay")
    print("""
  Coins
  Dollars
  Credit
""")
    what_user_wants = input("How do you want to pay? ")
    if what_user_wants == "Coins":
        coin_input = float(input("How much money? "))
        payment.take_coins_money(coin_input)
    elif what_user_wants == "Dollars":
        dollar_input = int(input("How many dollars? "))
        payment.take_physical_money(dollar_input)
    elif what_user_wants == "Credit":
        payment.validate_credit_card()
    else:
        print("You typed something invalid!")

def selection():
    pass

i_dont_want_to_quit = True

while i_dont_want_to_quit:
    print("Things you can do:")
    print("""
        Pay
        Select
        Quit
    """
    )
    what_user_wants = input("What do you want to do?")

    if what_user_wants == "Pay":
        pay()
    elif what_user_wants == "Select":
        selection()
    elif what_user_wants == "Quit":
        i_dont_want_to_quit = False
    else:
        print("Invalid choice")

print("Have a nice die")