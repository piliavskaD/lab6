import math

a = int(input("a = "))
b = int(input("b = "))
h = int(input("h = "))

def f(x):
    return (math.sin(x) * math.cos(2 * x)) / math.pow(3, 2 * x - 1)

A = []
B = []

x = a

for i in range(a, b + 1):
    y = f(x)
    A.append(y)
    B.append(y)
    x = x + h


small = min(A)
ind_small = A.index(small)
A = A[:ind_small + 1]

for res1 in A:
    print(res1)
    
big = max(B)
ind_big = B.index(big)
B = B[ind_big:]


print()
for res2 in B:
    print(res2)



common_words = set(A).intersection(B)
print(list(common_words))