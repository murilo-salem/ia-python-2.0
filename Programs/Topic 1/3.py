import math

def Area_Triangulo(a, b, c):
    S = (a + b + c) / 2
    Area = math.sqrt(S * (S - a) * (S - b) * (S - c))
    return Area

