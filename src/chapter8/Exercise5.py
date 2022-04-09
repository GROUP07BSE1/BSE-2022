file_name = input("Enter a file name : ")
fhandle = open(file_name)
count = 0
for line in fhandle:
    if line.startswith("From") and not line.startswith("From:"):
        line = line.split()
        print(line[1])
        count += 1
print(f"There were {count} lines in the file with From as the first word")