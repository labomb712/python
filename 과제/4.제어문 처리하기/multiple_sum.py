multiples_of_3 = []
total_sum = 0

for num in range(1, 101):
    if num % 3 == 0:
        multiples_of_3.append(num)
        total_sum += num

count_of_multiples = len(multiples_of_3)

print(f"1부터 100까지 3의 배수: {multiples_of_3}")
print(f"3의 배수의 합: {total_sum}")
print(f"3의 배수의 개수: {count_of_multiples}개")