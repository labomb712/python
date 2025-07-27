import math

def calculate_statistics(numbers):
    if not numbers:
        return {
            "평균": None,
            "최댓값": None,
            "최솟값": None,
            "표준편차": None
        }

    average = sum(numbers) / len(numbers)

    max_value = max(numbers)
    min_value = min(numbers)

    sum_of_squared_diff = sum([(x - average) ** 2 for x in numbers])
    if len(numbers) > 1:
        variance = sum_of_squared_diff / (len(numbers) - 1)
    else:
        variance = 0

    standard_deviation = math.sqrt(variance)

    return {
        "평균": average,
        "최댓값": max_value,
        "최솟값": min_value,
        "표준편차": round(standard_deviation, 2)
    }

data = [10, 20, 30, 40, 50]
stats = calculate_statistics(data)

print(f"숫자들: {data}")
print(f"평균: {stats['평균']}")
print(f"최댓값: {stats['최댓값']}")
print(f"최솟값: {stats['최솟값']}")
print(f"표준편차: {stats['표준편차']}")