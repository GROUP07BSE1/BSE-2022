working_hours = float(input("enter hours: "))
rate = float(input("enter rate: " ))
pay = working_hours * rate

if working_hours < 40:
    print(pay)
else:
    basic_pay = 400
    excess_rate = working_hours - 40
    bonus = excess_rate * rate * 1.5
    pay2 = basic_pay + bonus
    print(pay2)
