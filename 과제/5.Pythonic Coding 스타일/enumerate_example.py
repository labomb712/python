# enumerate_example.py

fruits = ['사과', '바나나', '오렌지', '포도', '딸기']

print("과일 목록:")
# enumerate를 사용하여 리스트의 인덱스와 값을 함께 출력합니다.
# enumerate는 루프를 돌면서 각 항목의 인덱스와 값을 튜플 형태로 반환합니다.
for index, fruit in enumerate(fruits):
    print(f"{index}: {fruit}")