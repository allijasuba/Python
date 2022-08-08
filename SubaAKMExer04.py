import math

x = [input("Value of x for sine:\n"), input("Value of x for cosine:\n")]


try:
    x[0].isnumeric()
    x[1].isnumeric()
    x1 = float(x[0])
    x2 = float(x[1])
    sin = math.sin(x1)
    cos = math.cos(x2)
    Sum = (sin ** 2) + (cos ** 2)
    print("sine: ", sin, " cosine: ", cos, " sum: ", Sum)
except ValueError as v:
    if x[0].isnumeric():
        x1 = float(x[0])
        sin = math.sin(x1)
        print("sine: ", sin, " cosine:  ", v, " sum: ", v)
    elif x[1].isnumeric():
        x2 = float(x[1])
        cos = math.cos(x2)
        print("sine: ", v, " cosine:  ", cos, " sum: ", v)
    else:
        print("sine: ", v, " cosine:  ", v, " sum: ", v)