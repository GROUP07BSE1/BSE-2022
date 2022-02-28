list1 = []
count = 0
total = 0.0
sample = input("enter number:  ")
try:
    while sample != "done":
        count += 1
        value = float(sample)
        list1.append(value)
        total += value
        sample = input("enter number: ")

    print("list1: ", list1)

    print("The maximum number is: ", max(list1))

    print("The minimum number is: ", min(list1))

    print("Your total number of counts was: ", count)

    print("Your total addition of the numbers was: ", total)

    print("End of execution!")
except ValueError:
    print("Please enter numeric data....")
