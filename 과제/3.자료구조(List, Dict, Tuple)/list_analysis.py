a = [15,3,27,8,19,12,31]
print("숫자 목록:",a)

max_v = max(a)
print("최댓값:",max_v)

min_v = min(a)
print("최솟값:",min_v)

s = sorted(a)
if len(a) >= 2:
    second_value= s[-2]
    print(f"두 번째로 큰 값: {second_value}")
else:
    print("리스트에 두 번째로 큰 값을 찾을 만큼 충분한 숫자가 없습니다.")