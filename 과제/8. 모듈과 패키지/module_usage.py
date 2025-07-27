
import datetime
import random

print("현재 날짜와 시간:", datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

example_date = datetime.date(2025, 7, 20)
print(f"포맷된 날짜: {example_date.strftime('%Y년 %m월 %d일 %A')}")

print("임의의 숫자:", random.randint(1, 10)) 

print("임의의 실수:", round(random.uniform(1.0, 5.0), 2)) 

my_list = ['사과', '바나나', '오렌지', '포도', '딸기']
print("임의의 리스트 요소:", random.choice(my_list)) 

random.shuffle(my_list)
print("섞인 리스트:", my_list)