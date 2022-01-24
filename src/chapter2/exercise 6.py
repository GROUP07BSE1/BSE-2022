sample1 = input("x1")
sample2 = input("y1")
sample3 = input("x2")
sample4 = input("y2")
result1 = int(sample3) - int(sample1)
result2 = int(sample4) - int(sample2)
value1 = float(result1 ** 2) + float(result2 ** 2)
distance = value1 ** 0.5
print(distance)
