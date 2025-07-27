from math_operations import * 

radius = 5
area_of_circle = circle_area(radius)
print(f"원의 넓이: {area_of_circle:.2f}")

width = 10
height = 5
area_of_rectangle = rectangle_area(width, height)
print(f"직사각형 넓이: {area_of_rectangle}")

num_factorial = 5
factorial_result = factorial(num_factorial)
print(f"팩토리얼 {num_factorial}! = {factorial_result}")

num_a = 48
num_b = 18
gcd_result = gcd(num_a, num_b)
print(f"최대공약수({num_a}, {num_b}) = {gcd_result}")