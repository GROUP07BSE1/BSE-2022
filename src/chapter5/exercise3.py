# Group number: 07
# Group Members: IGA MARTIN, TUKASIIMA BLESSING, KEMBABAZI FANCY ORIKIRIZA, BESIGYE GERALD, KATUNGYE JAMSON,LOGWEE JONATHAN
# Date: Mon, feb21 2022
stock = [25, 25, 25, 0, 0]
actual_value = [0.05, 0.1, 0.25, 1, 5]
values = ["nickels", "dimes", "quarters", "ones", "fives"]
print("Welcome  to the vending machine change maker program\nChange maker initialized.")
quit = False
# Continue in loop provided the user doesn't quit
while quit != True:
    print(f"Stock contains: \n\t{int(stock[0])} {values[0]}\n\t{int(stock[1])} {values[1]}\n\t{int(stock[2])} {values[2]}\n\t{int(stock[3])} {values[3]}\n\t{int(stock[4])} {values[4]}")
    while True:
        # Asking for item price
        purchase_price = input("Enter the purchase price (xx.xx) or 'q' to quit: ")
        if purchase_price == "q":
            cents = (stock[0]*5 + stock[1]*10 + stock[2]*25 + stock[3]*100 + stock[4]*500)
            dollars = cents//100
            cents %= 100
            print(f"{dollars} dollars and {cents} cents")
            quit = True
            break
        else:
            price = float(purchase_price)
            # Checking if input is a valid multiple of 5 cents
            try:
                if (( price* 100) % 5) == 0:
                    print("Menu for deposits:\n\t'n'- deposit a nickel\n\t'd' - deposit a dime\n\t'q' - deposit a quarter\n\t'o' - deposit a one dollar bill\n\t'f' - deposit a five dollar bill\n\t'c' - cancel the purchase")
                    amount_to_pay = price
                    amount_to_be_returned = 0
                    # Continue in loop if the user still has a balance in payment
                    while amount_to_pay > 0:
                        if amount_to_pay > 1:
                            print(f"Payment Due: {int(amount_to_pay) } dollars and {(amount_to_pay - int(amount_to_pay))* 100}")
                        else:
                            print(f"Payment Due: {int(amount_to_pay *100)} cents")
                        deposit = input("Indicate your deposit")
                        count = 0
                        # Checking for the user's deposit
                        for i in "ndqof":
                            if deposit == i:
                                stock[count] = stock[count] + 1
                                amount_to_pay = amount_to_pay - actual_value[count]
                            count += 1
                            # Checking if the user has cancelled their purchase
                        if deposit == "c":
                            amount_to_be_returned = float(price) - amount_to_pay
                            break
                            # If the user has deposited more than necessary then he heeds a refund
                        if amount_to_pay < 0:
                            amount_to_be_returned = - (amount_to_pay)
                        # These take care of the refunding of the user
                    if amount_to_be_returned > 0:
                        print("Please take the change below")
                        e = 0
                        for i in range(3):
                            if stock[2 - i] >=((amount_to_be_returned*100)//((actual_value[2 - i])*100)):
                                e +=  ((amount_to_be_returned*100)//((actual_value[2 - i])*100)) * actual_value[2 - i]
                                stock[2 - i] -=((amount_to_be_returned*100)//((actual_value[2 - i])*100))
                                if ((amount_to_be_returned*100)//((actual_value[2 - i])*100)) > 0:
                                    print(f"{((amount_to_be_returned*100)//((actual_value[2 - i])*100))} {values[2 - i]}\n")
                                amount_to_be_returned -= ((amount_to_be_returned*100)//((actual_value[2 - i])*100)) * actual_value[2-i]
                            else:
                                print(f"{stock[2-i]} {values[2-i]}")
                                e += stock[2 - i] * actual_value[2 - i]
                                stock[2 - i] -= stock[2 - i]
                                amount_to_be_returned -= stock[2 -i] * actual_value[2-i]
                                # This deals with whether the machine has no more change
                        if int(amount_to_be_returned) > 0:
                            print("Machine out of change\nPlease visit the store manager for your change")
                            if amount_to_be_returned * 100 >= 100:
                                print(f"{((int((amount_to_be_returned*100))- (e * 100))//100)} dollars and {(amount_to_be_returned * 100) - int(amount_to_be_returned *100)} cents")
                            else:
                                print(f"{int(amount_to_be_returned) * 100} cents")
                            break
                        else:
                            print("Please ake the change below")
                            print("No change due \n")
                            break
                else:
                    print("Illegal price: Must be a non negative multiple of 5 cents")
            except:
                print("Illegal price: Must be a non negative multiple of 5 cents")


