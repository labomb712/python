

def factorial_recursive(n):
    """
    재귀 함수를 사용하여 팩토리얼을 계산합니다.
    n이 0 또는 1일 경우 1을 반환하고, 그렇지 않으면 n * factorial_recursive(n-1)을 호출합니다.
    """
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial_recursive(n - 1)

def factorial_iterative(n):
    """
    반복문을 사용하여 팩토리얼을 계산합니다.
    1부터 n까지의 숫자를 곱해 나갑니다.
    """
    if n < 0:
        raise ValueError("팩토리얼은 음수에 대해 정의되지 않습니다.")
    
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

print(f"5! (재귀) = {factorial_recursive(5)}")
print(f"5! (반복) = {factorial_iterative(5)}")
print(f"7! (재귀) = {factorial_recursive(7)}")
print(f"7! (반복) = {factorial_iterative(7)}")