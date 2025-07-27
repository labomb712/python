
coordinates = (10, 20)
x, y = coordinates
print(f"좌표: x={x}, y={y}")

numbers = [1, 2, 3]
a, b, c = numbers
print(f"리스트 언패킹: a={a}, b={b}, c={c}")


def sum_all_args(*args):
    total = 0
    for num in args:
        total += num
    return total

result = sum_all_args(10, 20, 30)
print(f"가변 인수의 합: {result}")

def print_kwargs(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}={value}", end=", ")
    print() # 줄바꿈

print("키워드 인수들:", end=" ")
print_kwargs(name="김철수", age=25, city="서울")