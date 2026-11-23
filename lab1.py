import math

def arcctg(x):
    return math.pi / 2 - math.atan(x)

def f(x):
    return (
        math.sin(25 / 54)
        - 18 * math.pi
        - 49 * math.e * 6 / ((x + 4) * (x - 10))
        + 14 * arcctg(x + 8)
        - 8 / (x + 15)
    )

x = float(input("Введите x: "))
try:
    print(f"f({x}) = {f(x)}")
except ZeroDivisionError:
    print("x попадает в точку разрыва (x = -15, -4 или 10)")