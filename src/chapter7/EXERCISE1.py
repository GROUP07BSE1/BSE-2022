file = input("Enter a file name: ")
with open(file, "r") as myfile:
    for line in myfile:
        line = line.rstrip()
        print(line.upper())
