import math

x = [input("Angle for sine:\n"), input("Angle for cosine:\n")]


def radian(degrees):
    return degrees * math.pi/180


try:
    x[0].isnumeric()
    x[1].isnumeric()
    x1 = float(x[0])
    x2 = float(x[1])
    sin = math.sin(radian(x1))
    cos = math.cos(radian(x2))
    Sum = (sin ** 2) + (cos ** 2)
    print("sine: ", sin, " cosine: ", cos, " sum: ", Sum)
except ValueError as v:
    if x[0].isnumeric():
        x1 = float(x[0])
        sin = math.sin(radian(x1))
        print("sine: ", sin, " cosine:  ", v, " sum: ", v)
    elif x[1].isnumeric():
        x2 = float(x[1])
        cos = math.cos(radian(x2))
        print("sine: ", v, " cosine:  ", cos, " sum: ", v)
    else:
        print("sine: ", v, " cosine:  ", v, " sum: ", v)