try:
    score = float(input("score"))
    if score > 1 or score < 0:
        raise ValueError
    if score >= 0.9:
        Grade = "A"
        print(Grade)
    elif score >= 0.8:
        Grade = "B"
        print(Grade)
    elif score >= 0.7:
        Grade = "C"
        print(Grade)
    elif score >= 0.6:
        Grade = "D"
        print(Grade)
    else:
        print("F")
except ValueError:
    print("bad score")





