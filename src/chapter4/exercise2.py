def investment():
    original_amount = input("C: ")
    amount_of_time = input("t: ")
    interest_rate = input("r: ")
    number_of_compounds = input("n: ")
    value1 = float(1) + float(interest_rate) / float(number_of_compounds)
    value2 = value1 ** (float(amount_of_time) * float(number_of_compounds))
    compound_interest = float(original_amount) * value2

    formated_amount_of_compound_interest = format(compound_interest, "0.2f")

    print("P", formated_amount_of_compound_interest)


investment()


