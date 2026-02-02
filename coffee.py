amount_due = 75

while amount_due > 0:
    print("amount__due:", amount_due)
    coin = int(input("Insert Coin:"))
    
    if coin in [50, 25, 10, 5, 1]:
        amount_due -= coin
        if amount_due < 0:
            print("Thank you for your payment.Here is your change:", -amount_due)
            change_owed = abs(amount_due)
           
            amount_due = 0
        else:
            print("Thank you for your payment. Amount due:", amount_due)
    else:
        print("Invalid coin. Please insert a valid coin.")
        