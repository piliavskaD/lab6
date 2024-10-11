import math

a = int(input("a = "))
b = int(input("b = "))
h = int(input("h = "))

B = []

x = a
while x <= b:
    y = (math.sin(x) * math.cos(2 * x)) / math.pow(3, 2 * x - 1)
    print(x, y)
    x = x + h
    