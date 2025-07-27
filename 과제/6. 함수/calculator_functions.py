def add(a, b):
    """두 수를 더합니다."""
    return a + b

def subtract(a, b):
    """두 수를 뺍니다."""
    return a - b

def multiply(a, b):
    """두 수를 곱합니다."""
    return a * b

def divide(a, b):
    """
    두 수를 나눕니다.
    나누는 수가 0인 경우 ZeroDivisionError를 발생시킵니다.
    """
    if b == 0:
        raise ZeroDivisionError("0으로 나눌 수 없습니다.")
    return a / b

num1 = 10
num2 = 5

print(f"{num1} + {num2} = {add(num1, num2)}")
print(f"{num1} - {num2} = {subtract(num1, num2)}")
print(f"{num1} * {num2} = {multiply(num1, num2)}")
print(f"{num1} / {num2} = {divide(num1, num2)}")