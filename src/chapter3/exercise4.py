try:
    age = int(input("How old are you ? "))
    if age >= 18:
        print("You can vote")
    elif age < 0:
        print("Time traveller ")
    else:
        print("Too young to vote ")
except ValueError:
    print("please enter values not characters")
finally:
    print("executing finally.....")
