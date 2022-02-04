work_place = input("location")
salary = int(input("pay"))
if salary >= 10000000 and work_place == "kampala":
    print("sure, i can work with it")
elif salary > 4000000 and work_place == "Mbarara":
    print("sure,i can work with this")
elif salary >= 0 and work_place == "space":
    print("sure, i can work with this")
elif salary < 1000000 and work_place == "kampala":
    print("no way !")
elif salary >= 6000000 and work_place:
    print("sure, i can work with this")
else:
    print("no thanks, i can find something better")
