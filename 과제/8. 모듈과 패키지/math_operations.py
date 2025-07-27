import math

PI = math.pi # 원주율 상수 정의

def circle_area(radius):
    return PI * (radius ** 2)

def rectangle_area(width, height):
    return width * height

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a