money = float(input("enter the amount to make change for"))
dollar_20 = money // 20
print(dollar_20, "twenties")

remainder = money % 20
dollar_10 = remainder // 10
print(dollar_10, "tens")

remainder2 = remainder % 10
dollar_5 = remainder2 // 5
print(dollar_5, "five")

remainder3 = remainder2 % 5
dollar_1 = remainder3 // 1
print(dollar_1, "ones")

remainder4 = remainder3 % 1
quarter = remainder4 // 0.25
print(quarter, "quarters")

remainder5 = remainder4 % 0.25
dime = remainder5 // 0.1
print(dime, "dimes")

remainder6 = remainder5 % 0.1
nickel = remainder6 // 0.05
print(nickel, "nickel")

remainder7 = remainder6 % 0.05
penny = remainder7 // 0.01
print(penny, "penny")
