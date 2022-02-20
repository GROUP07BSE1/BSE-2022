count = 0

total = 0.0

sample = input("enter number:  ")
try:
    while sample != "done":
        count += 1

        value = float(sample)
        total += value
        sample = input("enter number: ")
        average = total/count

    print("Your total number of counts was: ", count)

    print("Your total was: ", total)

    print("your average was: ", average)

    print("End of execution!")
except ValueError:
    print("Please enter numeric data....")
