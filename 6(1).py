import math

a = int(input("a = "))
b = int(input("b = "))
h = int(input("h = "))

A = list()
def f(x):
    return (math.sin(x) * math.cos(2 * x)) / math.pow(3, 2 * x - 1)

x = a


for i in range(a, b):
    y = f(x)
    print(x, y)
    x += h
