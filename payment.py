# Amount of money currently in the transaction
current_money = 0

# Price of soda
soda_price = .88

def validate_credit_card():
    pass

def charge_credit_card():
    pass

def return_credit_card():
    pass

def take_coins_money(amount):
    """
    Take coin money from a user
    :param amount:
    :return:
    """
    global current_money
    current_money = current_money + amount

def take_physical_money(amount):
    """
    Take dollar bills from a user
    :param amount:
    :return:
    """
    global current_money
    current_money = current_money + amount

def refund_physical_money():
    pass

def refund_coins_money():
    global current_money

    coins_list = [.25, .10, .05, .01]

    for coin in coins_list:
        coin_count = current_money // coin
        print("Returning {}".format(coin_count * coin))
        current_money = current_money - (coin_count * coin)

    if current_money > .001:
        print("ERROR: Money didn't equal 0 after refund")

def display_price():
    """
    Display the price for the soda

    * Didn't get a chance to use this one in lecture... *
    :return: None
    """
    global soda_price
    print("Price is: {}".format(soda_price))

def can_pay_for_soda():
    """
    :return: True if a user can pay for a soda yet
    """
    global soda_price, current_money
    if current_money >= soda_price:
        return True
    else:
        return False

def pay_for_soda():
    """
    Deduct the price of a soda from the current amount in the machine
    :return: None
    """
    global soda_price, current_money
    current_money = current_money - soda_price
