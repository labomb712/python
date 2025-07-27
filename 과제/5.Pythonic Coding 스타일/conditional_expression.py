score = 85
result = "합격" if score >= 80 else "불합격"
print(f"점수: {score}, 결과: {result}")

age = 17
status = "성년" if age >= 19 else "미성년자"
print(f"나이: {age}, 상태: {status}")
num1 = 42
num2 = 27
max_value = num1 if num1 > num2 else num2
print(f"숫자들의 최대값: {max_value}")
numbers = [-2, 5, 0, 12, -7, 8, 23, -1]
positive_numbers = [num for num in numbers if num > 0]
print(f"양수들: {positive_numbers}")