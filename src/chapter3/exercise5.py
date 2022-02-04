try:
    guests = int(input("Number of people turning up : "))
    if guests <= 50:
        print("$4,000")
    elif guests <= 100:
        print("$10,000")
    elif guests <= 200:
        print("$15,000")
    else:
        print("$20,000")
except ValueError:
    print("please enter numeric information")
finally:
    print("thanks for entrusting your function to us")
    