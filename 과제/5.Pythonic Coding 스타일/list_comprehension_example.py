numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(f"원본 리스트: {numbers}")

# 리스트 컴프리헨션을 사용하여 짝수만 추출
# numbers 리스트에서 각 num에 대해 num을 2로 나누었을 때 나머지가 0인 경우(짝수)에만 num을 포함합니다.
even_numbers = [num for num in numbers if num % 2 == 0]
print(f"짝수들: {even_numbers}")

# 리스트 컴프리헨션을 사용하여 짝수들을 제곱
# even_numbers 리스트의 각 num에 대해 num을 제곱한 값을 포함합니다.
squared_evens = [num ** 2 for num in even_numbers]
print(f"짝수의 제곱: {squared_evens}")